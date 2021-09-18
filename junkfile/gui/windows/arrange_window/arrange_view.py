# IMPORT QT CORE
from qt_core import *
from junkfile.gui.windows.arrange_window.typings import View


# MAIN WINDOW
class QtView(View):
    def setup(self, controller):

        # INITIALIZE SETTINGS
        self.get_settings_values()
        self.directory_in = self.settings_variables.value("directory_in")
        self.directory_out = self.settings_variables.value("directory_out")
        self.copy = self.settings_variables.value("copy", 0)
        self.height = self.settings_window.value("height", 300)
        self.width = self.settings_window.value("width", 650)

        # CREATE MAIN WIDGET
        self.main = QWidget()
        self.main.resize(self.width, self.height)
        self.main.setWindowTitle("Junkfile organizer")

        # initialize windows event
        self.main.closeEvent = self.close_event

        # CREATE MAIN LAYOUT
        self.layout = QGridLayout(self.main)
        self.layout.setContentsMargins(10, 5, 10, 5)
        self.layout.setHorizontalSpacing(5)
        self.layout.setVerticalSpacing(10)

        img = QImage("junkfile\gui\images\logo.png")
        pixmap = QPixmap(img.scaledToHeight(32))
        self.image = QLabel()
        self.image.setPixmap(pixmap)

        # ///////////////////////////////////////////////////////////////
        # CREATE DIRECTORY ORIGIN LABEL
        self.label_origin = QLabel("Choose a origin directory:")

        # CREATE TEXTLINE DIRECTORY ORIGIN
        self.directory_in = QLineEdit(self.directory_in)
        self.directory_in.setReadOnly(True)

        # CREATE BUTTON DIRECTORY ORIGIN
        self.button_directory_in = QPushButton("Open...")
        self.button_directory_in.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_directory_in.clicked.connect(controller.handle_dialog_directory_in)

        # CREATE DIRECTORY DESTINY LABEL
        self.label_destiny = QLabel("Choose a destiny directory:")

        # CREATE TEXTLINE DIRECTORY DESTINY
        self.directory_out = QLineEdit(self.directory_out)
        self.directory_out.setReadOnly(True)

        # CREATE BUTTON DIRECTORY DESTINY
        self.button_directory_out = QPushButton("Open...")
        self.button_directory_out.setSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Expanding
        )
        self.button_directory_out.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_directory_out.clicked.connect(
            controller.handle_dialog_directory_out
        )

        # CREATE CHECKBOX
        self.checkbox_copy = QCheckBox("Would you like o make a copy?")
        self.checkbox_copy.setChecked(self.copy)

        # ADD PROGRESSBAR
        self.progressbar = self.create_progressbar()

        # ADD LOG PANEL
        self.text_log = QPlainTextEdit()
        self.text_log.setReadOnly(True)

        # CREATE ARRANGE BUTTON
        self.button_arrange = QPushButton("Arrange")
        self.button_arrange.resize(250, 50)
        self.button_arrange.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_arrange.clicked.connect(controller.handle_arrange)

        # ADD WIDGETS
        # ///////////////////////////////////////////////////////////////

        # GROUP ORIGIN
        self.layout.addWidget(self.label_origin, 0, 0, 1, 3)
        self.layout.addWidget(self.directory_in, 1, 0)
        self.layout.addWidget(self.button_directory_in, 1, 2)

        # GROUP DESTINY
        self.layout.addWidget(self.label_destiny, 2, 0, 1, 3)
        self.layout.addWidget(self.directory_out, 3, 0)
        self.layout.addWidget(self.button_directory_out, 3, 2)

        # COPY OPTION
        self.layout.addWidget(self.checkbox_copy, 4, 0)

        self.layout.addWidget(self.progressbar, 5, 0, 1, 3)

        # LOG
        self.layout.addWidget(self.text_log, 6, 0, 1, 3)

        # ARRANGE BUTTON
        self.layout.addWidget(self.button_arrange, 7, 0, 1, 3)

        # ADD IMAGE
        self.layout.addWidget(self.image, 8, 0, 1, 3, alignment=Qt.AlignCenter)

        # SET CENTRAL WIDGET
        self.main.setLayout(self.layout)

    def create_progressbar(self):
        progressbar = QProgressBar()
        progressbar.setMinimum(0)
        progressbar.setMaximum(100)
        return progressbar

    def add_progresbar_value(self, value=0):
        self.progressbar.setValue(value)

    def get_progresbar_value(self):
        return self.progressbar.value()

    def get_settings_values(self):
        """create setting variable to retrieve in the next time the window open"""
        self.settings_window = QSettings("junkfile", "Window")
        self.settings_variables = QSettings("junkfile", "Variables")

    def close_event(self, event):
        """run when window close"""
        self.settings_window.setValue("height", self.main.rect().height())
        self.settings_window.setValue("width", self.main.rect().width())
        self.settings_variables.setValue("directory_in", self.directory_in.text())
        self.settings_variables.setValue("directory_out", self.directory_in.text())
        self.settings_variables.setValue(
            "copy", 1 if self.checkbox_copy.isChecked() else 0
        )

    def show(self) -> None:
        """show windows"""
        self.main.show()

    # ITERFACE HANDLERS
    def set_directory_in(self, path) -> None:
        self.directory_in.setText(path)

    def set_directory_out(self, path) -> None:
        self.directory_out.setText(path)

    def get_directory_in(self) -> str:
        return self.directory_in.text()

    def get_directory_out(self) -> str:
        return self.directory_out.text()

    def get_copy(self) -> bool:
        return self.checkbox_copy.isChecked()

    def append_text_log(self, item) -> None:
        self.text_log.appendPlainText(item)

    def delete_text_log(self) -> None:
        self.text_log.setPlainText("")
