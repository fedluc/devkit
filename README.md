# devkit

`devkit` is a Python package and CLI for developers maintaining Python packages
with native C or C++ bindings. It centralizes build, test, deploy, and cleanup
workflows behind a single YAML configuration file.

## Status

This repository contains the first implementation pass with:

- YAML configuration via `devkit.yml`
- Profile-based overrides
- Built-in adapters for CMake, `python -m build`, `pytest`, `tox`, `ctest`, and
  Twine uploads
- CLI commands for `build`, `test`, `deploy`, `clean`, and `validate`

## Quick Start

1. Install the package in editable mode:

```bash
pip install -e .[test]
```

2. Add a `devkit.yml` file to your project.

3. Run commands such as:

```bash
devkit validate
devkit build --profile mpi
devkit test --runner unit
devkit deploy --profile release --dry-run
```

See [`examples/qupled/devkit.yml`](examples/qupled/devkit.yml) for a concrete
configuration derived from the current `qupled` workflow.
