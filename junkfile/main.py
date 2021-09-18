# ///////////////////////////////////////////////////////////////
#
# BY: IVAN JOSE FREZZA JUNIOR
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT MODULES
import sys

# IMPORT QT CORE
from qt_core import *

# IMPORT STYLE
from junkfile.gui import themes

# IMPORT MAIN WINDOW
from junkfile.gui.windows.arrange_window import ArrangeWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("junkfile/gui/images/icon.ico"))

    arrangeWindow = ArrangeWindow()
    arrangeWindow.show()

    # APPLY STYLE
    themes.apply_stylesheet(app)

    # start app
    sys.exit(app.exec())
