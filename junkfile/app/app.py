from pathlib import Path

# modules
from junkfile.app.core import arrange
from junkfile.app import checks

from junkfile.app.log_listener import setup_log_event_handlers

# setup event listener
setup_log_event_handlers()


def run(dir_in: str, dir_out: str = None, copy: bool = False) -> None:
    """main script run"""

    # convert str to Path type
    home_dir = Path(dir_in)

    # check if directory out was informed
    if not dir_out or dir_out == dir_in:
        # build a path equal to dir_in but with -copy at the end
        dir_out = Path(dir_in).parent.joinpath(str(Path(dir_in).stem) + "-copy")
    else:
        # if directory was passed, check if it's valid.
        checks.is_valid(dir_out)
        dir_out = Path(dir_out)

    dest_dir = dir_out

    # check if is a valid directory
    checks.is_valid(home_dir)

    # arrange
    arrange(home_dir, dest_dir, copy)
