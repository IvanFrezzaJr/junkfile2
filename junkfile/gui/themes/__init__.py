from qt_core import QDir
from pathlib import Path
import os

# APPLY STYLE
# root directory
theme_folder = Path(__file__).resolve().parent


def apply_stylesheet(app, name="default"):

    theme_path = Path.joinpath(theme_folder, name)

    # create alias icon for the custom.qss file
    QDir.addSearchPath("icon", str(theme_path))

    stylesheet = app.styleSheet()
    with open(str(Path.joinpath(theme_path, "style.qss"))) as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
