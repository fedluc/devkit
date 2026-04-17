# 04-pybind11-profiles

This example keeps the tested mixed C++/Python project shape and adds
profile-driven build modes for the C++ side.

It shows:

- a default debug-oriented C++ build
- a `release` profile with a separate build directory and `Release` flags
- matching `ctest` runs for both build modes
- a Dockerfile that installs `foga` through `uv sync` and native tooling through
  `foga install --target system`

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
foga build python
foga build cpp
foga build --profile release cpp
foga test
foga test --profile release cpp
foga lint
```

Useful follow-up commands:

```bash
foga inspect --profile release build cpp
foga clean
```
