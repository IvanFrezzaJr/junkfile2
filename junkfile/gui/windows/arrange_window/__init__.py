from gui.windows.arrange_window.arrange_controller import Controller
from gui.windows.arrange_window.arrange_model import Model
from gui.windows.arrange_window.arrange_view import QtView
from junkfile.app.event import subscribe


class ArrangeWindow:
    def __init__(self):
        self.instance = Controller(Model(), QtView())

        self.setup_event_handlers()

    def show(self):
        self.instance.start()

    def setup_event_handlers(self):
        subscribe("ui_log", self.instance.handle_log)
        subscribe("ui_progressbar", self.instance.handle_progressbar)
