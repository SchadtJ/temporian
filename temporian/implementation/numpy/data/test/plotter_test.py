from absl.testing import parameterized, absltest

import matplotlib
import numpy as np

from temporian.implementation.numpy.data import plotter
from temporian.implementation.numpy.data.io import event_set


class PlotterTest(parameterized.TestCase):
    def setUp(self):
        # Make sure that the plot functions don't fail on command line
        print("Setting matplotlib backend to: agg")
        matplotlib.use("agg")

    @parameterized.parameters((True,), (False,))
    def test_plot(self, interactive):
        try:
            import IPython.display
        except ImportError:
            # IPython is not installed / supported
            return

        evset = event_set(
            timestamps=[0.1, 0.2, 0.3, 0.4, 0.5],
            features={
                "a": [1, 2, 3, 7, 8],
                "b": [4, 5, 6, 9, 10],
                "c": ["X", "Y", "X", "X", "Z"],
                "x": [1, 1, 1, 2, 2],
            },
            indexes=["x"],
        )

        _ = plotter.plot(
            evset, indexes=None, interactive=interactive, return_fig=True
        )
        _ = plotter.plot(
            evset, indexes=1, interactive=interactive, return_fig=True
        )
        _ = plotter.plot(
            evset, indexes=[1, 2], interactive=interactive, return_fig=True
        )
        _ = plotter.plot(
            evset,
            indexes=[(1,), (2,)],
            interactive=interactive,
            return_fig=True,
        )

    def test_index_str(self):
        try:
            import IPython.display
        except ImportError:
            # IPython is not installed / supported
            return

        evset = event_set(
            timestamps=[0.1, 0.2, 0.3],
            features={
                "a": [1, 2, 3],
                "b": [4, 5, 6],
                "c": ["X", "Y", "X"],
                "x": [1, 1, 1],
            },
            indexes=["c"],
        )

        _ = plotter.plot(evset, indexes="X", return_fig=True)
        _ = plotter.plot(evset, indexes=b"X", return_fig=True)
        _ = plotter.plot(evset, indexes=["X", "Y"], return_fig=True)
        _ = plotter.plot(evset, indexes=[("X",), ("Y",)], return_fig=True)

    def test_is_uniform(self):
        self.assertTrue(plotter.is_uniform([]))
        self.assertTrue(plotter.is_uniform([1]))
        self.assertTrue(plotter.is_uniform([1, 2, 3]))
        self.assertFalse(plotter.is_uniform([1, 2, 2.5]))

    def test_merged_plots(self):
        x1 = np.arange(200)
        evset_1 = event_set(
            timestamps=x1,
            features={
                "a": np.sin(x1 / 4),
                "b": np.sin(x1 / 2),
                "c": np.sin(x1 / 6),
            },
        )

        x2 = np.arange(200, 300)
        evset_2 = event_set(timestamps=x2, features={"d": np.sin(x2 / 8)})

        plot = plotter.plot(
            [
                evset_1["a"],
                (evset_1["a"],),
                evset_1[[]],
                (evset_1[["b", "c"]], evset_2),
            ],
            return_fig=True,
            interactive=True,
        )
        # plot.savefig("/tmp/fig.png")

        # plot.show()

        # from bokeh.io import export_svg

        # export_png(plot, filename="/tmp/fig.png")


if __name__ == "__main__":
    absltest.main()
