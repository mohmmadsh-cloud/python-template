"""Find files whose names start with 'deep'."""

from pathlib import Path


def thats_the_way(folder_path):
    """
    Return names of files starting with 'deep' in the given folder.
    """
    folder = Path(folder_path)

    return [
        item.name
        for item in folder.iterdir()
        if item.is_file() and item.name.startswith("deep")
    ]


if __name__ == "__main__":
    print(thats_the_way("src"))
