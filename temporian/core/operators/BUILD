package(
    default_visibility = ["//visibility:public"],
    licenses = ["notice"],
)

# Libraries
# =========

py_library(
    name = "operators_without_implementation",
    srcs_version = "PY3",
    deps = [
        ":fillna",
    ],
)

py_library(
    name = "base",
    srcs = ["base.py"],
    srcs_version = "PY3",
    deps = [

        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "cast",
    srcs = ["cast.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/data:node",
        "//temporian/core/data:schema",
        "//temporian/proto:core_py_proto",
        "//temporian/implementation/numpy/data:dtype_normalization",
    ],
)

py_library(
    name = "glue",
    srcs = ["glue.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/core/data:schema",
        "//temporian/proto:core_py_proto",
        "//temporian/utils:typecheck",
    ],
)

py_library(
    name = "lag",
    srcs = ["lag.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:duration_utils",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "leak",
    srcs = ["leak.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:duration_utils",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "filter",
    srcs = ["filter.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
        "//temporian/core/data:duration_utils",
    ],
)

py_library(
    name = "rename",
    srcs = ["rename.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/core/data:schema",
        "//temporian/proto:core_py_proto",
        "//temporian/utils:typecheck",
    ],
)

py_library(
    name = "drop_index",
    srcs = ["drop_index.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/core/data:schema",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "select",
    srcs = ["select.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/core/data:schema",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "add_index",
    srcs = ["add_index.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        ":drop_index",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/core/data:schema",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "prefix",
    srcs = ["prefix.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "propagate",
    srcs = ["propagate.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        ":resample",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "resample",
    srcs = ["resample.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "since_last",
    srcs = ["since_last.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "unique_timestamps",
    srcs = ["unique_timestamps.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
        "//temporian/utils:typecheck",
    ],
)

py_library(
    name = "begin",
    srcs = ["begin.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "end",
    srcs = ["end.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "tick",
    srcs = ["tick.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:duration_utils",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "unary",
    srcs = ["unary.py"],
    srcs_version = "PY3",
    deps = [
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/data:node",
        "//temporian/core/operators:base",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "join",
    srcs = ["join.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/data:node",
        "//temporian/core/data:schema",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "timestamps",
    srcs = ["timestamps.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "enumerate",
    srcs = ["enumerate.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "combine",
    srcs = ["combine.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
        "//temporian/utils:typecheck",
    ],
)

py_library(
    name = "fast_fourier_transform",
    srcs = ["fast_fourier_transform.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
    ],
)

py_library(
    name = "map",
    srcs = ["map.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:dataclasses",
        "//temporian/core:operator_lib",
        "//temporian/core/data:node",
        "//temporian/core/data:schema",
        "//temporian/proto:core_py_proto",
        "//temporian/core/data:dtype",
        "//temporian/core:typing",
        "//temporian/implementation/numpy/data:dtype_normalization",
        "//temporian/utils:typecheck",
        "//temporian/core:compilation",
    ],
)

py_library(
    name = "tick_calendar",
    srcs = ["tick_calendar.py"],
    srcs_version = "PY3",
    deps = [
        # already_there/numpy
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
        "//temporian/utils:typecheck",
    ],
)

py_library(
    name = "select_index_values",
    srcs = ["select_index_values.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core:typing",
        "//temporian/core/data:node",
        "//temporian/implementation/numpy/data:dtype_normalization",
        "//temporian/proto:core_py_proto",
        "//temporian/utils:typecheck",
    ],
)

py_library(
    name = "until_next",
    srcs = ["until_next.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:compilation",
        "//temporian/core:operator_lib",
        "//temporian/core/data:duration_utils",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
        "//temporian/utils:typecheck",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
    ],
)

py_library(
    name = "filter_moving_count",
    srcs = ["filter_moving_count.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:operator_lib",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
        "//temporian/core:typing",
        "//temporian/core/data:duration_utils",
        "//temporian/utils:typecheck",
        "//temporian/core:compilation",
    ],
)

py_library(
    name = "where",
    srcs = ["where.py"],
    srcs_version = "PY3",
    deps = [
        ":base",
        "//temporian/core:operator_lib",
        "//temporian/core/data:node",
        "//temporian/proto:core_py_proto",
        "//temporian/core:typing",
        "//temporian/utils:typecheck",
        "//temporian/core:compilation",
        "//temporian/core/data:dtype",
    ],
)


py_library(
    name = "fillna",
    srcs = ["fillna.py"],
    srcs_version = "PY3",
    deps = [
        "//temporian/core/data:node",
        "//temporian/core:typing",
        "//temporian/core/data:dtype",
        "//temporian/core/operators:glue",
        "//temporian/utils:typecheck",
        "//temporian/core:compilation",
    ],
)
