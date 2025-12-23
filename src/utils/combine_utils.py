from pathlib import Path
import random

def combine_shuffle_paths(
    splits_by_class: dict[str, dict[str, list[Path]]],
    seed: int = 42) -> dict[str, list[Path]]:
  
  combined = {
      'train': [],
      'val': [],
      'test': []
  }

  for class_name, train_val_test in splits_by_class.items():
    combined['train'].extend(splits_by_class[class_name]['train'])
    combined['val'].extend(splits_by_class[class_name]['val'])
    combined['test'].extend(splits_by_class[class_name]['test'])

  rng = random.Random(seed)

  rng.shuffle(combined['train'])
  rng.shuffle(combined['val'])
  rng.shuffle(combined['test'])


  return combined