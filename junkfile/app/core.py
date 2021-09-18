# import time


from pathlib import Path

#  third party
from tqdm import tqdm

# modules
from junkfile.app.helpers import (
    list_files,
    copy_files,
    delete_directory,
    move_directory,
)

from junkfile.app.event import notify


def arrange(dir_src: Path, dir_dst: Path, copy=False) -> bool:
    """copy source directory to organized directory"""

    # notify file.log
    notify("file_log", f"Parameters: {dir_src=} {dir_dst=} {copy=}")

    # notify UI
    notify("ui_log", f"Parameters: {dir_src=} {dir_dst=} {copy=}")
    # initialize logs

    # copy files temp to new directory
    files = list_files(dir_src)

    # convert to list to the progressbar
    file_list = list(files)

    # get steps to the progressbar
    step = round(100 / len(file_list), 0)
    with tqdm(total=100) as pbar:
        for file in file_list:

            # progress bar setup
            pbar.update(step)
            notify("ui_progressbar", step)
            # time.sleep(0.1)

            # get file basename
            basename = file.name

            # get file extension if is file
            extension = file.suffix if file.is_file() else ""
            if extension:
                # build directory extensions path
                directory_extension = dir_dst.joinpath(extension)

                if not directory_extension.exists():
                    directory_extension.mkdir(parents=True, exist_ok=True)

                # build target directory
                target_directory = directory_extension.joinpath(basename)

                # copy files to the new directory
                copy_files(file, target_directory)

                notify("file_arranged", file, target_directory)
                notify("ui_log", target_directory)

    if not copy:
        delete_directory(dir_src)
        move_directory(dir_dst, dir_src)

    notify("file_log", "Done!")
    notify("ui_log", "Done!")

    return True
