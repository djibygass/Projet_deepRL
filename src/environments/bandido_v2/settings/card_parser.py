from abc import ABC, abstractmethod
from pathlib import Path
from src.environments.bandido_v2.settings import line_card_parser


class cardParser(ABC):

    @staticmethod
    def get_card_parser(file_path: Path):
        return line_card_parser.line_card_parser(file_path)

    @abstractmethod
    def get_copies_of_card(self) -> int:
        pass

    @abstractmethod
    def get_card(self):
        pass

    @abstractmethod
    def has_next_line(self) -> bool:
        pass
