from typing import Iterable

from src.data.ApiDataStore import ApiDataStore
from src.data.HtmlDataStore import HtmlDataStore
from src.data.LocalDbDataStore import LocalDbDataStore
from src.domain.PlayerRepository import PlayerRepository
from src.domain.mapper.PlayerMapper import PlayerMapper
from src.domain.model.Player import Player


class PlayerRepositoryImpl(PlayerRepository):

    def __init__(
            self,
            api_data_store: ApiDataStore,
            html_data_store: HtmlDataStore,
            local_db_data_store: LocalDbDataStore,
            mapper: PlayerMapper,
    ):
        self.api_data_store = api_data_store
        self.html_data_store = html_data_store
        self.local_db_data_store = local_db_data_store
        self.mapper = mapper

    def get_players(self) -> Iterable[Player]:
        players = self.api_data_store.get_players()
        return map(self.mapper.map, players)

    def get_players_from_db(self) -> Iterable[Player]:
        players = self.local_db_data_store.get_players()
        return players

    def migrate_files_from_html_to_api(self) -> None:
        players = self.html_data_store.get_players()
        self.api_data_store.save_players(players)

    def store_players_in_db(self, players: Iterable[Player]) -> None:
        self.api_data_store.save_players(players)

    def store_players_into_db(self, players: Iterable[Player]) -> None:
        self.local_db_data_store.save_players(players)
