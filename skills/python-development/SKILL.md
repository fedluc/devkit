---
name: python-development
description: Implement, refactor, review, and maintain modern Python projects with consistent repository standards. Use when Codex is editing Python source, tests, packaging metadata, or developer tooling and needs project-specific guidance for code structure, type hints, linting, formatting, and verification. Especially useful for tasks involving `pyproject.toml`, `src/`, `tests/`, CLI code, packaging, or changes that must satisfy `ruff`, `pytest`, and build validation.
---

# Python Development

Use this skill to keep Python changes small, typed, testable, and easy to verify.

## Workflow

* Use the workflow described at `docs/development.md`. 
* If any tools necessary to follow the workflow are missing notify the user.
* Inspect the existing module, tests, and `pyproject.toml` before changing behavior.
* Match the repository's current structure instead of introducing new abstractions by default.
* Prefer small pure functions, explicit data flow, and standard-library solutions unless the repo already depends on something heavier.
* Add or update tests in the same change when behavior changes.
* Run formatting, linting, and relevant tests before finishing.
* Review any touched Python docstrings before finishing and keep them in valid Google style.

## Coding Standards

* Target Python 3.10+ features already used by the repo.

### Type-hints

* Add type hints for public functions and for internal functions.
* Prefer `pathlib.Path`, `dataclass`, and straightforward collections over stringly-typed or deeply nested state.

### Docstrings

* When Python docstrings are added or touched, keep them in valid Google style. 
* Do not leave touched public functions, helpers, or dataclasses with placeholder one-line docstrings when parameters, return values, exceptions, or fields need explanation.

### Code structure

* Keep diffs consistent with surrounding code and existing module boundaries instead of introducing new multi-purpose modules.
* Raise precise exceptions with actionable messages.
* Keep functions focused. Split only when it improves readability or testability.
* Avoid thin wrapper helpers that only forward to another function or registry lookup.
* When multiple workflow sections share the same shape, prefer one shared parser or selection helper over copy-pasted loops.
* Avoid premature frameworks, dependency injection layers, or generic utility modules unless the codebase already uses them.
* Prefer `__future__.annotations` in Python modules when surrounding files use it.

### Comments

* Keep comments sparse. Add them only when behavior is non-obvious.

## Testing and Validation

* The testing workflow is documented in `docs/development.md` under "Run checks while developing". Use it. 
* Run targeted tests first when a narrow test file covers the change.
* Run `pytest` for any behavior change, bug fix, or CLI/config update.
* If CLI or config behavior changes, add or update CLI-facing and config-facing tests in the same change.
* If a command cannot be run, state that clearly and explain why.

### Testing Policy

* Add tests for new behavior and regressions.
* Prefer assertions on observable behavior, not implementation details.
* Keep fixtures local to the test module unless they are broadly reused.
* For CLI behavior, test exit codes and user-visible output.
* For config parsing, test both valid and invalid inputs.

## Ruff Policy

* Ruff usage is documented in `docs/development.md` under "Run checks while developing". Use it. 
* Fix lint violations in touched files rather than suppressing them by default.
* Add ignores only when the repository has a documented reason and the alternative is clearly worse.

## Packaging and Project Layout

* Keep application code under `src/` and tests under `tests/` when the repo already follows that layout.
* Keep tool configuration in `pyproject.toml`.
* Prefer PEP 621 metadata in `pyproject.toml`.
* Update the documentation if the development dependencies change 
* `foga` expects a root-level `foga.yml`.
* When configuration or adapter behavior changes, update `README.md` and relevant documentation.

## References

* Read [references/python-standards.md](references/python-standards.md) for the detailed checklist and code-review heuristics used by this skill.
