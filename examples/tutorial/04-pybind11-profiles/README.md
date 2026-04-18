# 04-pybind11-profiles

This example keeps the tested mixed C++/Python project shape and adds
profile-driven build modes for the C++ side.

It shows:

- a default debug-oriented C++ build
- a `release` profile with a separate build directory and `Release` flags
- matching `ctest` runs for both build modes
- a Docker image that installs `foga` from PyPI before you install the example
  package and native tooling inside the container

Files:

- [`Dockerfile`](Dockerfile)
- [`run-docker.sh`](run-docker.sh)
- [`foga.yml`](foga.yml)
- [`pyproject.toml`](pyproject.toml)
- [`cpp/`](cpp)
- [`src/hello_bindings`](src/hello_bindings)
- [`tests/`](tests)

## Start the example

```bash
./run-docker.sh
```

## Inside the container

Run these commands to verify the example:

```bash
foga validate
foga install --target system
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

The example runs directly in the container's Python environment without a
separate project virtual environment. The container also shows a short
instructions file automatically when the interactive shell starts.
