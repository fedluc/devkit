# 01-python-only

This is the smallest runnable `foga` example in the repository.

## What You Learn

- how to start from a minimal `foga` project
- how to validate a config before running workflows
- how to build and install a Python package through `foga`

## Local prerequisites

- Python 3.10+
- `foga`

## Run locally

```bash
foga validate
foga install --target dev
foga build
vector-demo
foga inspect
```

## Docker shortcut

From the repository root:

```bash
python examples/tutorial/run-example.py 01-python-only
```

Then run the same `foga` commands inside the container shell.
