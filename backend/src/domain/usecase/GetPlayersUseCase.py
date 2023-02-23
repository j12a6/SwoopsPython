from typing import Iterable

from src.domain.PlayerRepository import PlayerRepository
from src.domain.model import Player


class GetPlayersUseCase:

    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def execute(self) -> Iterable[type[Player]]:
        return self.player_repository.get_players_from_db()
