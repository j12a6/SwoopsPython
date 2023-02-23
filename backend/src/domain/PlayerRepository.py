from abc import abstractmethod
from typing import Protocol, Iterable

from src.domain.model.Player import Player


class PlayerRepository(Protocol):

    @abstractmethod
    def get_players(self) -> Iterable[Player]:
        pass

    @abstractmethod
    def get_players_from_db(self) -> Iterable[Player]:
        pass

    @abstractmethod
    def store_players_into_db(self, players: Iterable[Player]) -> None:
        pass

    @abstractmethod
    def migrate_files_from_html_to_api(self) -> None:
        pass
