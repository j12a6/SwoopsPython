import os
from pathlib import Path

from src.data.ApiDataStore import ApiDataStore
from src.data.HtmlDataStore import HtmlDataStore
from src.data.LocalDbDataStore import LocalDbDataStore
from src.data.PathProvider import PathProvider
from src.data.PlayerRepositoryImpl import PlayerRepositoryImpl
from src.domain.PlayerRepository import PlayerRepository
from src.domain.mapper.PlayerMapper import PlayerMapper


def provide_PathProvider() -> PathProvider:
    return PathProvider(
        api_path=os.path.join(str(Path.home()), "Projects/databases/swoops/players/"),
        local_db_path=os.path.join(str(Path.home()), "Projects/Swoops/frontend/instance/front.sqlite"),
    )


def provide_ApiDatastore() -> ApiDataStore:
    return ApiDataStore(provide_PathProvider())


def provide_HtmlDataStore() -> HtmlDataStore:
    return HtmlDataStore(provide_PathProvider())


def provide_LocalDbDataStore() -> LocalDbDataStore:
    return LocalDbDataStore(provide_PathProvider())


def provide_PlayerRepository() -> PlayerRepository:
    return PlayerRepositoryImpl(
        provide_ApiDatastore(),
        provide_HtmlDataStore(),
        provide_LocalDbDataStore(),
        PlayerMapper(),
    )
