# 03-pybind11-tests

This example keeps the mixed C++/Python project shape from the previous step
and adds both test workflows and Python linting.

It shows:

- Python tests for the `pybind11` module
- C++ tests driven through `ctest`
- Python `ruff format` and `ruff check` targets
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
foga build cpp
./build-cpp/hello_cli
foga build python
foga test
foga format --dry-run
foga lint
foga inspect test
foga clean
```

The example runs directly in the container's Python environment without a
separate project virtual environment. The container also shows a short
instructions file automatically when the interactive shell starts.
