from pathlib import Path
import random
from typing import Optional

def sample_list(
    paths: list[Path],
    sample_size: Optional[int],
    seed: int = 42
) -> list[Path]:

  if not isinstance(paths, list):
      raise TypeError("paths must be a list of Path objects")

  if not paths:
      raise ValueError("paths list is empty")

  if sample_size is None:
      return paths

  if not isinstance(sample_size, int):
      raise TypeError(f"sample_size must be int or None; got {type(sample_size)}")

  if sample_size < 0:
      raise ValueError(f"sample_size must be non-negative; got {sample_size}")

  if sample_size > len(paths):
      raise ValueError(
          f"sample_size ({sample_size}) exceeds number of paths ({len(paths)})"
      )

  rng = random.Random(seed)
  return rng.sample(paths, sample_size)


def sample_paths_by_class(
    paths_by_class: dict[str, list[Path]],
    sample_size: Optional[int],
    seed: int = 42
) -> dict[str, list[Path]]:

  if not isinstance(paths_by_class, dict):
      raise TypeError("paths_by_class must be a dict")

  sampled = {}

  for class_name, paths in paths_by_class.items():
    sampled[class_name] = sample_list(
        paths=paths,
        sample_size=sample_size,
        seed=seed
    )

  return sampled