import json
import os
from typing import Iterable

from src.data.PathProvider import PathProvider
from src.data.model.PlayerDto import PlayerDto


class ApiDataStore:

    def __init__(self, path_provider: PathProvider):
        self.path_provider = path_provider

    def get_players(self) -> Iterable[PlayerDto]:
        player_ids = self.__get_player_ids()
        return map(self.__get_player, player_ids)

    def __get_player(self, player_id: str) -> PlayerDto:
        dir_path = self.path_provider.get_players_api_dir_path()
        filename = self.path_provider.get_player_api_filename(player_id)
        file_path = f"{dir_path}{filename}"
        json_data = self.__load_json_from_api_file(file_path)
        return PlayerDto(number=player_id, traits=json_data["traits"])

    def save_players(self, players: Iterable[PlayerDto]) -> None:
        for player in players:
            self.__save_player(player)

    def __get_player_ids(self) -> Iterable[str]:
        dir_path = self.path_provider.get_players_api_dir_path()
        filenames = self.__get_filenames(dir_path)
        return map(self.__get_player_id_from_filename, filenames)

    def __save_player(self, player) -> None:
        dir_path = self.path_provider.get_players_api_dir_path()
        filename = self.path_provider.get_player_api_filename(player.number)
        file_path = f"{dir_path}{filename}"
        with open(file_path, "w") as f:
            json.dump({"traits": player.traits}, f, indent=4)

    @staticmethod
    def __get_filenames(path: str) -> list[str]:
        return list(file for file in os.listdir(path) if file.endswith(".json"))

    @staticmethod
    def __get_player_id_from_filename(filename: str) -> str:
        return filename.replace("player_", "").replace(".json", "")

    @staticmethod
    def __load_json_from_api_file(path: str) -> dict:
        with open(path, "r") as f:
            json_data = json.load(f)
            return json_data
