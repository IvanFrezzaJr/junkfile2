# IMPORT QT CORE
from qt_core import *
from app.app import run
from junkfile.gui.windows.arrange_window.typings import View, Model


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.show()

    def handle_dialog_directory_in(self):
        """call dialog window"""
        self.model.directory_in = QFileDialog.getExistingDirectory(
            None, "Select Directory"
        )
        if self.model.directory_in:
            self.view.set_directory_in(self.model.directory_in)

        if not self.model.directory_out:
            self.model.directory_out = self.model.directory_in
            self.view.set_directory_out(self.model.directory_out)

    def handle_dialog_directory_out(self):
        """call dialog window"""
        self.model.directory_out = QFileDialog.getExistingDirectory(
            None, "Select Directory"
        )

        if not self.model.directory_out:
            self.view.set_directory_in(self.model.directory_out)

    def handle_arrange(self):
        """call arrange function"""
        self.view.add_progresbar_value(0)

        # get data from UI
        self.model.directory_in = self.view.get_directory_in()
        self.model.directory_out = self.view.get_directory_out()
        self.model.copy = self.view.get_copy()

        # clean text log
        self.view.delete_text_log()

        # run arrange function
        run(
            dir_in=self.model.directory_in,
            dir_out=self.model.directory_out,
            copy=self.model.copy,
        )

    def handle_log(self, item):
        """call view log function to append log"""
        self.view.append_text_log(str(item))

    def handle_progressbar(self, step):
        old_value = self.view.get_progresbar_value() or 0

        """call view log function to append log"""
        self.view.add_progresbar_value(int(old_value + step))
