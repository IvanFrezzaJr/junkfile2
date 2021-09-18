from pathlib import Path
import shutil


def list_files(dir_path: Path, pattern: str = "*") -> list:
    paths = []
    for path in dir_path.rglob(pattern):
        paths.append(path)

    return paths


def copy_files(file_src: Path, file_dst: Path) -> bool:
    """copy file"""
    try:
        shutil.copyfile(file_src, file_dst)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        return False
    return True


def move_directory(dir_src: str, dir_dst: str) -> bool:
    try:
        shutil.move(dir_src, dir_dst)

    except OSError as error:
        print(error)
        return False

    return True


def delete_directory(path: Path) -> True:
    """delete directory"""

    if not path or not path.exists():
        return False

    return shutil.rmtree(path, ignore_errors=True)
