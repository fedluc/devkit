from __future__ import annotations

import numpy as np
from rich.console import Console


def centered_norm(values: list[float]) -> float:
    data = np.asarray(values, dtype=float)
    centered = data - data.mean()
    return float(np.linalg.norm(centered))


def main() -> None:
    vector = [1.0, 2.0, 3.0]
    norm = centered_norm(vector)
    Console().print(f"Centered norm for {vector}: {norm:.3f}")


if __name__ == "__main__":
    main()
