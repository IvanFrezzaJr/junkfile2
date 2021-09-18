import os
from pathlib import Path
from junkfile.app.helpers import list_files


def is_valid(path: Path) -> bool:

    """loop through the list of files and check permission"""
    if not path.is_dir():
        raise Exception(f"Directory not valid. {path}")

    for item in list_files(path):
        if not check_permission(item):
            raise Exception(f"You don't have permission to access {item} file.")

        # check if is not inthe blacklist directory
        if item in get_blacklist_directories():
            raise Exception(f"Directory {item} can't be selected")

    return True


def check_permission(path: str) -> bool:
    """Check permission"""

    return (
        all(
            (
                check_exists(path),
                check_is_readable(path),
                check_is_writable(path),
                check_is_executable(path),
            )
        )
        if path
        else False
    )


def check_exists(path: str) -> bool:
    """Check if the file exists"""

    return os.access(path, os.F_OK) if path else False


def check_is_readable(path: str) -> bool:
    """Check if the file is readable"""

    return os.access(path, os.R_OK) if path else False


def check_is_writable(path: str) -> bool:
    """Check if the file is writable"""

    return os.access(path, os.W_OK) if path else False


def check_is_executable(path: str) -> bool:
    """Check if the file is executable"""

    return os.access(path, os.X_OK) if path else False


def get_blacklist_directories() -> list:
    """list of OS directories"""
    return [
        "c:/",
        "d:/",
        "/",
        "/bin",
        "/etc",
        "/lib",
        "/lib64",
        "/run",
        "/sbin",
        "/sys",
        "/proc",
        "/root",
        "/srv",
        "/usr",
    ]
