# observer
subscribers = dict()


def subscribe(event_type: str, fn):
    """add new event in the listener"""
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def unsubscribe(event_type: str) -> None:
    if event_type in subscribers:
        del subscribers[event_type]


def notify(event_type: str, *args, **kwargs):
    """notify events"""
    if event_type not in subscribers:
        return None
    for fn in subscribers[event_type]:
        fn(*args, **kwargs)
