# Getting Started

This guide will help you get started with `temporian`.

## Installation

Temporian is available on PyPI. To install it, run:

```shell
pip install temporian
```

## A Minimal End-to-End Run

A minimal end-to-end run looks as follows:

```python
import temporian as tp

# Load the data
event_data = tp.read_event("path/to/data.csv")
event = event_data.schema()

# Compute features
# TODO: complete with a simple example...

```

## Main concepts

- [Event](../reference/temporian/core/data/event/) is the main concept in Temporian. It represents a collection of time series data. Each time series is identified by a unique feature name. Each time series is a sequence of values, each value is associated with a timestamp. The timestamps are assumed to be in ascending order.

- [Feature](../reference/temporian/core/data/feature/) is a single time series in an event. It is identified by a unique name within the event. Each feature has a specific type.

- TODO: add more concepts here...