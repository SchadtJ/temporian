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

import numpy as np

from temporian.core.data.sampling import Sampling
from temporian.core.operators.propagate import propagate
from temporian.core.data import event as event_lib
from temporian.core.data.feature import Feature
from temporian.core.data.dtype import DType


class PropagateOperatorTest(absltest.TestCase):
    def setUp(self):
        pass

    def test_basic(self):
        event = event_lib.input_event(
            [
                Feature("a", DType.FLOAT64),
                Feature("b", DType.FLOAT64),
            ],
            sampling=Sampling(index_levels=[("x", DType.STRING)]),
        )
        sampling = event_lib.input_event(
            [],
            sampling=Sampling(
                index_levels=[("x", DType.STRING), ("y", DType.STRING)]
            ),
        )
        _ = propagate(event=event, sampling=sampling)

    def test_error_wrong_index(self):
        event = event_lib.input_event(
            [
                Feature("a", DType.FLOAT64),
                Feature("b", DType.FLOAT64),
            ],
            sampling=Sampling(index_levels=[("z", DType.STRING)]),
        )
        sampling = event_lib.input_event(
            [],
            sampling=Sampling(
                index_levels=[("x", DType.STRING), ("y", DType.STRING)]
            ),
        )
        with self.assertRaisesRegex(
            ValueError,
            "The index of event should be contained in the index of sampling",
        ):
            _ = propagate(event=event, sampling=sampling)

    def test_error_wrong_index_type(self):
        event = event_lib.input_event(
            [
                Feature("a", DType.FLOAT64),
                Feature("b", DType.FLOAT64),
            ],
            sampling=Sampling(index_levels=[("x", DType.INT32)]),
        )
        sampling = event_lib.input_event(
            [],
            sampling=Sampling(
                index_levels=[("x", DType.STRING), ("y", DType.STRING)]
            ),
        )
        with self.assertRaisesRegex(
            ValueError,
            "However, the dtype is different",
        ):
            _ = propagate(event=event, sampling=sampling)


if __name__ == "__main__":
    absltest.main()
