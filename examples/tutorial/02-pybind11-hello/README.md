# 02-pybind11-hello

This example adds a tiny `pybind11` module while keeping the standalone C++
build separate from the Python package build.

It shows:

- a small shared C++ greeting implementation
- a standalone CMake executable built through `build cpp`
- a Python package built through `build python`
- a Dockerfile that installs `foga` through `uv sync` and native tooling through
  `foga install --target system`

Files:

- [`Dockerfile`](Dockerfile)
- [`run-docker.sh`](run-docker.sh)
- [`foga.yml`](foga.yml)
- [`pyproject.toml`](pyproject.toml)
- [`cpp/`](cpp)
- [`src/hello_bindings`](src/hello_bindings)

## Start the example

```bash
./run-docker.sh
```

## Inside the container

Run these commands to verify the example:

```bash
foga validate
foga install --target dev
foga build cpp
foga build python
```

Useful follow-up commands:

```bash
foga inspect build cpp
foga clean
```
