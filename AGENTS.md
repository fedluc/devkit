# Repository Guidelines

## Project Structure & Module Organization

Application code lives under `src/devkit/`. Keep CLI entrypoints in `src/devkit/cli.py`, shared config handling in `src/devkit/config.py`, execution helpers in `src/devkit/executor.py`, and backend-specific command builders in `src/devkit/adapters/`. Tests live in `tests/` and currently cover config loading, adapter behavior, and CLI routing. Example user configuration lives in `examples/qupled/devkit.yml`. Use `README.md` for end-user setup and `REMAINING_PLAN.md` for unfinished product work.

## Build, Test, and Development Commands

Set up a local environment with:

```bash
pip install -e .[dev]
```

Run the test suite with:

```bash
pytest
```

Lint the code with:

```bash
ruff check .
```

Validate packaging metadata with:

```bash
python -m build
```

Exercise the CLI during development with commands such as `devkit validate`, `devkit build --profile mpi`, and `devkit deploy --dry-run`. When using the devcontainer, `.devcontainer/post-create.sh` installs the same editable development environment automatically.

## Coding Style & Naming Conventions

Target Python 3.10+ and use 4-space indentation. Follow existing module boundaries instead of adding large multi-purpose files. Prefer descriptive snake_case for functions, variables, and test names; keep class names in PascalCase. Match the repository’s current style: small focused functions, straightforward control flow, and minimal comments unless behavior is non-obvious. Run `ruff check .` for linting and keep diffs consistent with surrounding code.

## Testing Guidelines

Use `pytest` for all tests. Add new tests in `tests/` with filenames named `test_<area>.py` and test functions named `test_<behavior>()`. Cover both happy paths and invalid configuration or command-generation cases. Run `ruff check .` and `pytest` before merging. If you change CLI behavior, add or update CLI-facing tests before merging.

## Commit & Pull Request Guidelines

Recent commits use short, imperative subjects such as `Add devcontainer bootstrap and development docs`. Keep commit titles concise and specific. Pull requests should explain the user-facing change, note any config or CLI behavior differences, and list the verification performed, for example `ruff check .`, `pytest`, or a representative `devkit ... --dry-run` command. Include sample output only when it clarifies behavior.

## Configuration Notes

`devkit` expects a root-level `devkit.yml`. When adding new configuration fields or adapter behavior, update `README.md` and the example in `examples/qupled/devkit.yml` so the documented workflow stays accurate.
