from pathlib import Path

def make_labeled_items(
    paths: list[Path],
    class_to_ids: dict[str, int]
) -> list[tuple[Path, int]]:

    items = []

    for path in paths:
        class_name = path.parent.name.lower()

        if class_name not in class_to_ids:
            raise ValueError(f"Unknown class folder: {class_name}")

        items.append((path, class_to_ids[class_name]))

    return items

def build_labeled_splits(
    combined_splits: dict[str, list[Path]]
) -> dict[str, list[tuple[Path, int]]]:

    class_to_ids = {"cat": 0, "dog": 1}

    return {
        "train": make_labeled_items(combined_splits["train"], class_to_ids),
        "val":   make_labeled_items(combined_splits["val"],   class_to_ids),
        "test":  make_labeled_items(combined_splits["test"],  class_to_ids),
    }
