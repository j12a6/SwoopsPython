import os
from pathlib import Path


class PathProvider:

    def __init__(self, api_path: str, local_db_path: str):
        self.api_path = api_path
        self.local_db_path = local_db_path
        self.local_db_schema = os.path.join(str(Path.home()), "Projects/Swoops/frontend/front/schema.sql")

    def get_players_api_dir_path(self) -> str:
        return self.api_path

    def get_local_db_file_path(self) -> str:
        return self.local_db_path

    @staticmethod
    def get_player_api_filename(player_id: str) -> str:
        return f"player_{player_id}.json"

    @staticmethod
    def get_players_html_dir_path() -> str:
        return "./../../databases/swoops/scrapped_html_pages/"

    @staticmethod
    def get_player_html_filename(player_id: str) -> str:
        return f"player_{player_id}.html"
