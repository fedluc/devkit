# 01-python-only

This is the smallest runnable `foga` example in the repository.

It shows:

- a pure Python package with `numpy` and `rich`
- a `uv`-based development install
- a `python-build` package build
- a dedicated Docker environment so the example does not touch the host machine
- a self-contained `uv` project that installs `foga` from PyPI

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
foga install --target dev
foga build
```

Useful follow-up commands:

```bash
foga inspect
foga clean
```
