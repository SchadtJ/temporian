"""Bokeh plotting backend."""

import datetime
from typing import Optional, List, Any, Set

import numpy as np
from temporian.core.data.duration_utils import (
    convert_timestamp_to_datetime,
    convert_timestamps_to_datetimes,
)

from temporian.implementation.numpy.data.event_set import EventSet, IndexType
from temporian.implementation.numpy.data.plotter import (
    Options,
    Style,
    is_uniform,
    get_num_plots,
    auto_style,
    Groups,
)


def plot_bokeh(
    groups: Groups,
    indexes: List[IndexType],
    options: Options,
):
    from bokeh.io import output_notebook, show
    from bokeh.layouts import gridplot
    from bokeh.models import CustomJS
    from bokeh.palettes import Dark2_5 as colors

    num_plots = get_num_plots(groups, indexes, options)

    figs = []

    index_names = groups[0].items[0].evtset.schema.index_names()

    # Actual plotting
    plot_idx = 0
    for index in indexes:
        assert len(index_names) == len(index)
        if plot_idx >= num_plots:
            # Too much plots are displayed already.
            break

        title = " ".join([f"{k}={v}" for k, v in zip(index_names, index)])

        # Index of the next color to use in the plot.
        color_idx = 0

        for group in groups:
            if plot_idx >= num_plots:
                break
            group_has_one_item = len(group.items) == 1

            for group_item in group.items:
                xs = group_item.evtset.data[index].timestamps
                uniform = is_uniform(xs)

                plot_mask = np.full(len(xs), True)
                if options.min_time is not None:
                    plot_mask = plot_mask & (xs >= options.min_time)
                if options.max_time is not None:
                    plot_mask = plot_mask & (xs <= options.max_time)
                if (
                    options.max_points is not None
                    and len(xs) > options.max_points
                ):
                    # Too many timestamps. Only keep the fist ones.
                    plot_mask = plot_mask & (
                        np.cumsum(plot_mask) <= options.max_points
                    )

                xs = xs[plot_mask]

                if group_item.evtset.schema.is_unix_timestamp:
                    # Matplotlib understands datetimes.
                    xs = convert_timestamps_to_datetimes(xs)

                if group_item.feature_idx == -1:
                    # There is not features to plot. Instead, plot the timestamps.
                    figs.append(
                        _bokeh_sub_plot(
                            xs=xs,
                            ys=np.zeros(len(xs)),
                            options=options,
                            color=colors[color_idx % len(colors)],
                            name="[sampling]",
                            is_unix_timestamp=group_item.evtset.schema.is_unix_timestamp,
                            title=title,
                            style=Style.vline,
                        )
                    )
                else:
                    feature_name = group_item.evtset.schema.features[
                        group_item.feature_idx
                    ].name

                    ys = group_item.evtset.data[index].features[
                        group_item.feature_idx
                    ]
                    ys = ys[plot_mask]
                    if options.style == Style.auto:
                        effective_stype = auto_style(uniform, xs, ys)
                    else:
                        effective_stype = options.style

                    figs.append(
                        _bokeh_sub_plot(
                            xs=xs,
                            ys=ys,
                            options=options,
                            color=colors[color_idx % len(colors)],
                            name=feature_name if group_has_one_item else None,
                            legend=(
                                feature_name if not group_has_one_item else None
                            ),
                            is_unix_timestamp=group_item.evtset.schema.is_unix_timestamp,
                            title=title,
                            style=effective_stype,
                        )
                    )

                # Only print the index / title once
                title = None

                color_idx += 1

            # if not group_has_one_item:
            #     axs[plot_idx, 0].legend(fontsize=8)

            plot_idx += 1

    if len(figs) > 1:
        # Sync x-axes
        js_vars = [f"p{fig_idx+1}_x_range" for fig_idx, fig in enumerate(figs)]
        js_inputs = {}
        core_code = ""
        for js_var, fig in zip(js_vars, figs):
            js_inputs[js_var] = fig.x_range

            sub_core_code = "\n".join(
                [
                    f"""
            {other_js_var}.start = start;
            {other_js_var}.end = end;
            """
                    for other_js_var in js_vars
                    if other_js_var != js_var
                ]
            )

            core_code += f"""
            if (cb_obj == {js_var}) {{
                const start =  {js_var}.start;
                const end =  {js_var}.end;
                {sub_core_code}
            }}
            """

        callback = CustomJS(args=js_inputs, code=core_code)

        for fig in figs:
            fig.x_range.js_on_change("start", callback)
            fig.x_range.js_on_change("end", callback)

        figure_set = gridplot(
            [[f] for f in figs],
            merge_tools=True,
            toolbar_location="right",
            toolbar_options=dict(logo=None),
        )
    else:
        figure_set = figs[0]
        figure_set.toolbar.logo = None

    output_notebook(hide_banner=True)
    show(figure_set)
    return figure_set


def _bokeh_sub_plot(
    xs,
    ys,
    options: Options,
    color,
    name: Optional[str],
    is_unix_timestamp: bool,
    title: Optional[str],
    style: Style,
    legend: Optional[str] = None,
) -> Any:
    """Plots "(xs, ys)" on the axis "ax"."""

    from bokeh.plotting import figure
    from bokeh.models import Range1d

    tools = [
        "xpan",
        "pan",
        "xwheel_zoom",
        "ywheel_zoom",
        "box_zoom",
        "reset",
        "undo",
        "save",
        "hover",
    ]

    fig_args = {}
    if is_unix_timestamp:
        fig_args["x_axis_type"] = "datetime"
    if title:
        fig_args["title"] = title

    is_string = ys.dtype.type is np.str_ or ys.dtype.type is np.bytes_
    if is_string:
        ys = ys.astype(np.str_)
        unique_ys_values = list(set(ys))
        fig_args["y_range"] = unique_ys_values
    else:
        unique_ys_values = None

    fig = figure(
        width=options.width_px,
        height=options.height_per_plot_px,
        tools=tools,
        **fig_args,
    )

    if options.min_time is not None or options.max_time is not None:
        args = {}
        if options.min_time is not None:
            args["start"] = (
                convert_timestamp_to_datetime(options.min_time)
                if is_unix_timestamp
                else options.min_time
            )
        if options.max_time is not None:
            args["end"] = (
                convert_timestamp_to_datetime(options.max_time)
                if is_unix_timestamp
                else options.max_time
            )
        fig.x_range = Range1d(**args)

    data = {"x": xs, "y": ys, "color": color}

    if is_string:
        fig.circle(x=xs, y=ys)
    elif style == Style.line:
        fig.line(**data)
    elif style == Style.marker:
        fig.scatter(**data)
    elif style == Style.vline:
        fig.scatter(**data)
    else:
        raise ValueError("Non implemented style")

    if name is not None:
        fig.yaxis.axis_label = name

    return fig
