from src.domain.model import Player
from src.domain.PlayerRepository import PlayerRepository


class MigrateFilesFromHtmlToApiUseCase:

    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def execute(self) -> Player:
        return self.player_repository.migrate_files_from_html_to_api()
