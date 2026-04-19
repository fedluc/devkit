# 04-pybind11-profiles

This example keeps the mixed C++/Python project shape from the previous example
and adds profile-driven build modes for the C++ side.

## What You Learn

- how to use profiles to switch between debug and release C++ builds
- how to keep one example config while varying build and test behavior by profile
- how to compare default and release workflows from the same tutorial
- how to grow a validated example without duplicating the whole setup

## Local prerequisites

- Python 3.10+
- `foga`
- a C++ compiler
- CMake
- Ninja

## Run locally

```bash
foga validate
foga install --target dev
foga build python
foga build cpp
foga build --profile release cpp
foga test
foga test --profile release cpp
foga format --dry-run
foga lint
foga inspect --profile release build cpp
foga clean
```

## Docker shortcut

From the repository root:

```bash
python examples/tutorial/run-example.py 04-pybind11-profiles
```

Then run `foga install --target system` once inside the container, followed by
the same commands shown above.
