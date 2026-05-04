# Contributing to foga

Thank you for taking the time to improve `foga`. Contributions can be bug
reports, documentation fixes, example improvements, tests, or code changes.

## Before You Start

For larger changes, please open or check an issue first so the approach can be
discussed before implementation. Small fixes, documentation edits, and clear
test improvements are welcome directly as pull requests.

Keep changes focused. A small pull request that solves one problem is easier to
review and safer to merge than one that changes several unrelated things.

## Project Layout

- `src/foga/` contains the package and CLI implementation.
- `src/foga/cli/` contains CLI entrypoints and command wiring.
- `src/foga/config/` contains configuration loading, parsing, and models.
- `src/foga/adapters/` contains backend-specific command builders.
- `tests/` contains the test suite.
- `examples/` contains example projects and tutorials.
- `docs/` contains the documentation site.

## Development Setup

The main contributor setup is documented in
[`docs/development.md`](docs/development.md). In short, install `uv`, then sync
the development and documentation dependencies:

```bash
uv sync --extra dev --extra docs
```

## Running Checks

Run the fast checks while developing:

```bash
uv run ruff format .
uv run ruff check .
uv run pytest
```

If you change documentation, also build the docs with warnings treated as
errors:

```bash
uv run sphinx-build -W --keep-going -b html docs docs/_build/html
```

Before release-oriented changes, check that the package can be built:

```bash
uv run python -m build
```

## Tests and Documentation

Add or update tests for behavior changes. Update documentation or examples when
a change affects user-facing commands, configuration, output, or recommended
workflows.

Prefer straightforward code that matches the existing style. Avoid adding new
abstractions, options, or dependencies unless they clearly solve the problem at
hand.

## Bug Reports

Useful bug reports include:

- The operating system and Python version.
- The installed `foga` version or commit.
- The command you ran.
- The relevant `foga.yml`, if applicable.
- The behavior you expected.
- The behavior you saw instead, including the full error output when possible.

## Pull Requests

Before opening a pull request, please:

- Keep the change focused on one issue or improvement.
- Include tests for behavior changes.
- Update docs or examples for user-facing changes.
- Run the relevant checks and mention them in the pull request description.
- Link any related issue.
- Call out compatibility, packaging, or documentation impact when relevant.
