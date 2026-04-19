#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def available_examples(tutorial_root: Path) -> list[str]:
    """Return the tutorial directories that provide a Docker shortcut."""
    return sorted(
        path.name
        for path in tutorial_root.iterdir()
        if path.is_dir() and (path / "Dockerfile").is_file()
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command line arguments for the tutorial runner."""
    parser = argparse.ArgumentParser(
        description="Build and run a tutorial example in Docker."
    )
    parser.add_argument("example", nargs="?")
    parser.add_argument(
        "--list",
        action="store_true",
        help="Print the available examples and exit.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Build and run the selected tutorial container."""
    args = parse_args(argv or sys.argv[1:])
    tutorial_root = Path(__file__).resolve().parent
    examples = available_examples(tutorial_root)

    if args.list:
        print("\n".join(examples))
        return 0

    if args.example not in examples:
        print("Choose one of the available examples:", file=sys.stderr)
        for example in examples:
            print(f"  - {example}", file=sys.stderr)
        return 2

    if shutil.which("docker") is None:
        print("Docker is required but was not found.", file=sys.stderr)
        return 1

    example_dir = tutorial_root / args.example
    image_name = f"foga-tutorial-{args.example}"

    print(f"Setting up example environment for {args.example}")

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as build_log:
        build_log_path = Path(build_log.name)

    try:
        with build_log_path.open("w", encoding="utf-8") as stream:
            result = subprocess.run(
                ["docker", "build", "--no-cache", "-t", image_name, str(example_dir)],
                stdout=stream,
                stderr=subprocess.STDOUT,
                check=False,
            )

        if result.returncode != 0:
            print("Docker image build failed. Full output follows:")
            print(build_log_path.read_text(encoding="utf-8"), end="")
            return result.returncode

        print("Environment ready.")
        print("You will be dropped into the container, where you can run the example.")
        print('Run "exit" to leave the container.')
        print()
        print("Entering container...")
        print()

        run_result = subprocess.run(
            ["docker", "run", "--rm", "-it", image_name, "bash", "-i"],
            check=False,
        )
        return run_result.returncode
    finally:
        build_log_path.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
