# 03-pybind11-tests

This example keeps the mixed C++/Python project shape from the previous step
and adds both test workflows and Python linting.

It shows:

- Python tests for the `pybind11` module
- C++ tests driven through `ctest`
- Python `ruff format` and `ruff check` targets
- a Dockerfile that installs `foga` through `uv sync` and the native build
  toolchain through `foga install --target system`

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
foga install --target dev
foga build
foga test
foga lint
```

Useful follow-up commands:

```bash
foga inspect test
foga clean
```
