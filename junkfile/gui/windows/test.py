from junkfile.app.event_class import Observable, Observer
from typing import List
from dataclasses import dataclass


@dataclass
class ArrangeObservable(Observable):

    __observers: List[Observer] = []

    def __init__(self, input):
        self.input = input

    def subscribe(self, observers: List[Observer]) -> None:
        for observer in observers:
            if observer in self.__observers:
                return None
            self.__observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self.__observers:
            del self.__observers[observer]

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self)
