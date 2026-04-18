#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EXAMPLE_NAME = "pybind11-tests"
IMAGE_NAME = "foga-tutorial-pybind11-tests"


def main() -> int:
    """Build and run the tutorial container."""
    if shutil.which("docker") is None:
        print("Docker is required but was not found on PATH.", file=sys.stderr)
        return 1

    script_dir = Path(__file__).resolve().parent

    print(f"Setting up example environment for {EXAMPLE_NAME}")

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as build_log:
        build_log_path = Path(build_log.name)

    try:
        with build_log_path.open("w", encoding="utf-8") as stream:
            result = subprocess.run(
                ["docker", "build", "--no-cache", "-t", IMAGE_NAME, str(script_dir)],
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
            ["docker", "run", "--rm", "-it", IMAGE_NAME, "bash", "-i"],
            check=False,
        )
        return run_result.returncode
    finally:
        build_log_path.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
