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
import pandas as pd

from temporian.core.operators.calendar.minute import (
    CalendarMinuteOperator,
)
from temporian.implementation.numpy.data.event import IndexData
from temporian.implementation.numpy.data.event import NumpyEvent
from temporian.implementation.numpy.operators.calendar.minute import (
    CalendarMinuteNumpyImplementation,
)


class CalendarMinuteNumpyImplementationTest(absltest.TestCase):
    """Test numpy implementation of calendar_minute operator."""

    def test_basic(self) -> None:
        "Basic test with flat event."
        input_event_data = NumpyEvent.from_dataframe(
            pd.DataFrame(
                data=[
                    [pd.to_datetime("1970-01-01 00:00:00", utc=True)],
                    [pd.to_datetime("2023-01-01 00:01:00", utc=True)],
                    [pd.to_datetime("2023-01-01 00:30:00", utc=True)],
                    [pd.to_datetime("2023-01-01 00:59:00", utc=True)],
                    [pd.to_datetime("2023-01-01 23:01:00", utc=True)],
                    [pd.to_datetime("2023-01-01 23:59:59", utc=True)],
                ],
                columns=["timestamp"],
            ),
        )
        input_event = input_event_data.schema()
        output_event_data = NumpyEvent(
            data={
                (): IndexData(
                    [np.array([0, 1, 30, 59, 1, 59]).astype(np.int32)],
                    input_event_data.first_index_data().timestamps,
                ),
            },
            feature_names="calendar_minute",
            index_names=[],
            is_unix_timestamp=True,
        )
        operator = CalendarMinuteOperator(input_event)
        impl = CalendarMinuteNumpyImplementation(operator)
        output = impl.call(sampling=input_event_data)

        self.assertTrue(output_event_data == output["event"])
        self.assertTrue(
            output["event"].first_index_data().features[0].dtype == np.int32
        )


if __name__ == "__main__":
    absltest.main()
