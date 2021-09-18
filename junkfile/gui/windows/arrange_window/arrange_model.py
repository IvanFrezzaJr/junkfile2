from dataclasses import dataclass


@dataclass
class Model:
    directory_in: str = ""
    directory_out: str = ""
    copy: bool = False
