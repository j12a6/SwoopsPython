from typing import Iterable

from src.domain.model import Player


class StoreInDbUseCase:

    def __init__(self):
        pass

    def execute(self, players: Iterable[type[Player]]) -> Iterable[type[Player]]:
        return [self.__update_player_skills(player) for player in players]
