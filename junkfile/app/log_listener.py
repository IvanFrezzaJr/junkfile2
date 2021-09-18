from junkfile.lib.log import log
from junkfile.app.event import subscribe


def handle_file_arranged_event(path_from, path_to):
    log(f"moved from {path_from} to {path_to}")


def handle_file_log_event(message):
    log(message)


def setup_log_event_handlers():
    subscribe("file_arranged", handle_file_arranged_event)
    subscribe("file_log", handle_file_log_event)
