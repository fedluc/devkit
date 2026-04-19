from __future__ import annotations

from rich.console import Console

from ._core import greet


def main() -> None:
    Console().print(f"python says: {greet('foga')}")


if __name__ == "__main__":
    main()
