# 02-pybind11-hello

This example adds a tiny `pybind11` module while keeping the standalone C++
build separate from the Python package build.

## What You Learn

- how to manage a mixed Python and C++ example with one `foga` config
- how to install native build tools through `foga`
- how to build the C++ and Python sides separately
- how to move from a pure Python example to a simple binding workflow

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
foga build cpp
./build-cpp/hello_cli
foga build python
hello-demo
foga inspect build cpp
```

## Docker shortcut

From the repository root:

```bash
python examples/tutorial/run-example.py 02-pybind11-hello
```

Then run `foga install --target system` once inside the container, followed by
the same commands shown above.
