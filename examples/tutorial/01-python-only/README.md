# 01-python-only

This is the smallest runnable `foga` example in the repository.

It shows:

- a pure Python package with `numpy` and `rich`
- a plain `pip`-based development install
- a `python-build` package build
- a dedicated Docker environment so the example does not touch the host machine
- a Docker image that installs `foga` from PyPI before installing the example package

Files:

- [`Dockerfile`](Dockerfile)
- [`run-docker.sh`](run-docker.sh)
- [`foga.yml`](foga.yml)
- [`pyproject.toml`](pyproject.toml)
- [`src/vector_demo`](src/vector_demo)

## Start the example

```bash
./run-docker.sh
```

## Inside the container

Run these commands to verify the example:

```bash
foga validate
foga build
foga install --target dev
vector-demo
foga inspect
```

The example runs directly in the container's Python environment without a
separate project virtual environment. The container also shows a short
instructions file automatically when the interactive shell starts.
