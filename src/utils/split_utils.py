from pathlib import Path
import random

def split_paths(
    paths: list[Path],
    ratios: tuple[float, float, float],
    seed: int = 42
) -> dict[str, list[Path]]:

    # ---- type & emptiness checks ----
    if not isinstance(paths, list):
        raise TypeError("paths must be a list of Path objects")
    if not paths:
        raise ValueError("paths list is empty")

    if not isinstance(ratios, tuple) or len(ratios) != 3:
        raise ValueError("ratios must be a tuple of (train, val, test)")

    train_r, val_r, test_r = ratios

    # ---- ratio validation ----
    if any(r < 0 for r in ratios):
        raise ValueError(f"ratios must be non-negative; got {ratios}")

    total = train_r + val_r + test_r
    if abs(total - 1.0) > 1e-9:
        raise ValueError(f"ratios must sum to 1.0; got {total}")
      
    rng = random.Random(seed)
    shuffled = list(paths)
    rng.shuffle(shuffled)

    # ---- split ----
    n = len(shuffled)
    train_end = int(train_r * n)
    val_end = train_end + int(val_r * n)

    train_paths = shuffled[:train_end]
    val_paths = shuffled[train_end:val_end]
    test_paths = shuffled[val_end:]

    return {
        "train": train_paths,
        "val": val_paths,
        "test": test_paths
    }
