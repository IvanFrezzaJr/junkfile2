from abc import ABC, abstractmethod

# VIEW INTERFACE
class View(ABC):
    @abstractmethod
    def setup(self, controller) -> None:
        ...

    @abstractmethod
    def set_directory_in(self, path: str) -> None:
        ...

    @abstractmethod
    def set_directory_out(self, path: str) -> None:
        ...

    @abstractmethod
    def get_directory_in(self) -> str:
        ...

    @abstractmethod
    def get_directory_out(self) -> str:
        ...

    @abstractmethod
    def get_copy(self) -> bool:
        ...

    @abstractmethod
    def append_text_log(self, item) -> None:
        ...

    @abstractmethod
    def delete_text_log(self) -> None:
        ...


class Model(ABC):
    ...
