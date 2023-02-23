from typing import Iterable

from src.domain.model import Player


class FilterOnPlayerNumbersUseCase:

    @staticmethod
    def execute(players: Iterable[type[Player]], player_numbers: list[str]) -> Iterable[type[Player]]:
        return [player for player in players if player.number in player_numbers]
