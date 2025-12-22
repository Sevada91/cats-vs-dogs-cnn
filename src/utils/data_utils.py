from pathlib import Path

def get_paths_by_class(root_dir: Path) -> dict[str, list[Path]]:    
    """
    Collect image file paths grouped by class from a dataset directory.

    The input path must be a directory whose final structure contains
    one subdirectory per class, specifically:

        root_dir/
            Cat/
            Dog/
    """

    # ---- Type & root validation ----
    if not isinstance(root_dir, Path):
        raise TypeError("root_dir must be a pathlib.Path")
    if not root_dir.exists():
        raise FileNotFoundError(f"Root directory '{root_dir}' does not exist.")
    if not root_dir.is_dir():
        raise NotADirectoryError(f"{root_dir} is not a directory.")

    # ---- Class directory validation (UPDATED) ----
    cat_dir = root_dir / "Cat"
    dog_dir = root_dir / "Dog"

    if not cat_dir.exists():
        raise FileNotFoundError(f"Cat directory '{cat_dir}' does not exist.")
    if not cat_dir.is_dir():                                  # ← ADDED
        raise NotADirectoryError(f"{cat_dir} is not a directory.")

    if not dog_dir.exists():
        raise FileNotFoundError(f"Dog directory '{dog_dir}' does not exist.")
    if not dog_dir.is_dir():                                  # ← ADDED
        raise NotADirectoryError(f"{dog_dir} is not a directory.")

    # ---- Initialize predictable output structure ----
    paths_by_class = {
        "cat": [],
        "dog": []
    }

    # ---- Allowed image types ----
    img_types = {".jpg", ".jpeg", ".png"}

    # ---- Collect image paths ----
    for img in cat_dir.rglob("*"):
        if img.is_file() and img.suffix.lower() in img_types:
            paths_by_class["cat"].append(img)

    for img in dog_dir.rglob("*"):
        if img.is_file() and img.suffix.lower() in img_types:
            paths_by_class["dog"].append(img)

    # ---- Empty-class protection (ADDED) ----
    if len(paths_by_class["cat"]) == 0:
        raise ValueError(f"No valid images found in '{cat_dir}'.")
    if len(paths_by_class["dog"]) == 0:
        raise ValueError(f"No valid images found in '{dog_dir}'.")


    return paths_by_class




