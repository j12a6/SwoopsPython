from src.domain.PlayerRepository import PlayerRepository
from src.domain.usecase.GetPlayersAfterSkillsUpdateUseCase import GetPlayersAfterSkillsUpdateUseCase


class ExportPlayersToDbUseCase:

    def __init__(
            self,
            get_player_after_skills_update_use_case: GetPlayersAfterSkillsUpdateUseCase,
            player_repository: PlayerRepository,
    ):
        self.get_player_after_skills_update_use_case = get_player_after_skills_update_use_case
        self.player_repository = player_repository

    def execute(self) -> None:
        players = self.player_repository.get_players()
        players = self.get_player_after_skills_update_use_case.execute(players)
        self.player_repository.store_players_into_db(players)
