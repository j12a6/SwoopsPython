import pickle
import sqlite3
from typing import Iterable

from src.data.PathProvider import PathProvider
from src.domain.model.Player import Player


class LocalDbDataStore:

    def __init__(self, path_provider: PathProvider):
        self.path_provider = path_provider
        conn = sqlite3.connect(self.path_provider.get_local_db_file_path())
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        if 'players' not in map(lambda xy: xy[0], tables):
            with open(path_provider.local_db_schema, 'r') as f:
                cursor.executescript(f.read())
        cursor.close()

    def get_players(self) -> Iterable[Player]:
        conn = sqlite3.connect(self.path_provider.get_local_db_file_path())
        cursor = conn.cursor()
        cursor.execute("SELECT player FROM players")
        for row in cursor:
            yield pickle.loads(row[0])
        cursor.close()

    def save_players(self, players: Iterable[Player]) -> None:
        conn = sqlite3.connect(self.path_provider.get_local_db_file_path())
        cursor = conn.cursor()
        for player in players:
            player_representation = pickle.dumps(player, pickle.HIGHEST_PROTOCOL)
            cursor.execute(
                'INSERT INTO players VALUES (?, ?)', (int(player.number), sqlite3.Binary(player_representation)),
            )
        conn.commit()
        conn.close()
