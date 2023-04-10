# Copyright 2021 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from absl.testing import absltest
import math

import pandas as pd
import numpy as np

from temporian.core.operators.window.moving_sum import (
    MovingSumOperator,
)
from temporian.implementation.numpy.operators.window.moving_sum import (
    MovingSumNumpyImplementation,
)
from temporian.implementation.numpy.data.event import NumpyEvent
from temporian.core.data import event as event_lib
from temporian.core.data import feature as feature_lib
from temporian.core.data import dtype as dtype_lib
import math
from temporian.implementation.numpy_cc.operators import window as window_cc
from numpy.testing import assert_array_equal


def _f64(l):
    return np.array(l, np.float64)


def _f32(l):
    return np.array(l, np.float32)


nan = math.nan


class MovingSumOperatorTest(absltest.TestCase):
    def test_cc_wo_sampling(self):
        assert_array_equal(
            window_cc.moving_sum(
                _f64([1, 2, 3, 5, 20]),
                _f32([10, nan, 12, 13, 14]),
                5.0,
            ),
            _f32([10.0, 10.0, 22.0, 35.0, 14.0]),
        )

    def test_flat(self):
        """A simple time sequence."""

        input_data = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    [10.0, 20.0, 1],
                    [11.0, 21.0, 2],
                    [12.0, 22.0, 3],
                    [13.0, 23.0, 5],
                    [14.0, 24.0, 20],
                ],
                columns=["a", "b", "timestamp"],
            )
        )

        op = MovingSumOperator(
            event=input_data.schema(),
            window_length=5,
            sampling=None,
        )
        self.assertEqual(op.list_matching_io_samplings(), [("event", "event")])
        instance = MovingSumNumpyImplementation(op)

        output = instance(event=input_data)

        expected_output = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    [10.0, 20.0, 1],
                    [21.0, 41.0, 2],
                    [33.0, 63.0, 3],
                    [46.0, 86.0, 5],
                    [14.0, 24.0, 20],
                ],
                columns=["a", "b", "timestamp"],
            )
        )

        self.assertEqual(repr(output), repr({"event": expected_output}))

    def test_with_index(self):
        """Indexed time sequences."""

        input_data = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    ["X1", "Y1", 10.0, 1],
                    ["X1", "Y1", 11.0, 2],
                    ["X1", "Y1", 12.0, 3],
                    ["X2", "Y1", 13.0, 1.1],
                    ["X2", "Y1", 14.0, 2.1],
                    ["X2", "Y1", 15.0, 3.1],
                    ["X2", "Y2", 16.0, 1.2],
                    ["X2", "Y2", 17.0, 2.2],
                    ["X2", "Y2", 18.0, 3.2],
                ],
                columns=["x", "y", "a", "timestamp"],
            ),
            index_names=["x", "y"],
        )

        op = MovingSumOperator(
            event=input_data.schema(),
            window_length=5,
            sampling=None,
        )
        self.assertEqual(op.list_matching_io_samplings(), [("event", "event")])
        instance = MovingSumNumpyImplementation(op)

        output = instance(event=input_data)

        expected_output = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    ["X1", "Y1", 10.0, 1],
                    ["X1", "Y1", 21.0, 2],
                    ["X1", "Y1", 33.0, 3],
                    ["X2", "Y1", 13.0, 1.1],
                    ["X2", "Y1", 27.0, 2.1],
                    ["X2", "Y1", 42.0, 3.1],
                    ["X2", "Y2", 16.0, 1.2],
                    ["X2", "Y2", 33.0, 2.2],
                    ["X2", "Y2", 51.0, 3.2],
                ],
                columns=["x", "y", "a", "timestamp"],
            ),
            index_names=["x", "y"],
        )

        self.assertEqual(output["event"], expected_output)

    def test_with_sampling(self):
        """Time sequenes with user provided sampling."""

        input_data = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    [10.0, 1],
                    [11.0, 2],
                    [12.0, 3],
                    [13.0, 5],
                    [14.0, 6],
                ],
                columns=["a", "timestamp"],
            )
        )

        op = MovingSumOperator(
            event=input_data.schema(),
            window_length=3.1,
            sampling=event_lib.input_event([]),
        )
        self.assertEqual(
            op.list_matching_io_samplings(), [("sampling", "event")]
        )
        instance = MovingSumNumpyImplementation(op)

        sampling_data = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    [-1.0],
                    [1.0],
                    [1.1],
                    [3.0],
                    [3.5],
                    [6.0],
                    [10.0],
                ],
                columns=["timestamp"],
            )
        )

        output = instance(event=input_data, sampling=sampling_data)

        expected_output = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    [0, -1.0],
                    [10.0, 1.0],
                    [10.0, 1.1],
                    [33.0, 3.0],
                    [33.0, 3.5],
                    [39.0, 6.0],
                    [0, 10.0],
                ],
                columns=["a", "timestamp"],
            )
        )

        self.assertEqual(output["event"], expected_output)

    def test_with_nan(self):
        """The input features contains nan values."""

        input_data = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    [math.nan, 1],
                    [11.0, 2],
                    [math.nan, 3],
                    [13.0, 5],
                    [14.0, 6],
                ],
                columns=["a", "timestamp"],
            )
        )

        op = MovingSumOperator(
            event=input_data.schema(),
            window_length=1.1,
            sampling=event_lib.input_event([]),
        )
        instance = MovingSumNumpyImplementation(op)

        sampling_data = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    [1],
                    [2],
                    [2.5],
                    [3],
                    [3.5],
                    [4],
                    [5],
                    [6],
                ],
                columns=["timestamp"],
            )
        )

        output = instance(event=input_data, sampling=sampling_data)

        expected_output = NumpyEvent.from_dataframe(
            pd.DataFrame(
                [
                    [0, 1],
                    [11.0, 2],
                    [11.0, 2.5],
                    [11.0, 3],
                    [0, 3.5],
                    [0, 4],
                    [13.0, 5],
                    [27.0, 6],
                ],
                columns=["a", "timestamp"],
            )
        )

        self.assertEqual(output["event"], expected_output)


if __name__ == "__main__":
    absltest.main()