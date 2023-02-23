from src.di.data.DataDi import provide_PlayerRepository
from src.domain.usecase.ExportPlayersToDbUseCase import ExportPlayersToDbUseCase
from src.domain.usecase.FilterOnInterestingPlayersUseCase import FilterOnInterestingPlayersUseCase
from src.domain.usecase.FilterOnPlayerNumbersUseCase import FilterOnPlayerNumbersUseCase
from src.domain.usecase.GetPlayersAfterSkillsUpdateUseCase import GetPlayersAfterSkillsUpdateUseCase
from src.domain.usecase.GetPlayersUseCase import GetPlayersUseCase


def provide_GetPlayersUseCase() -> GetPlayersUseCase:
    return GetPlayersUseCase(provide_PlayerRepository())


def provide_GetPlayersAfterSkillsUpdateUseCase() -> GetPlayersAfterSkillsUpdateUseCase:
    return GetPlayersAfterSkillsUpdateUseCase()


def provide_ExportPlayersToDbUseCase() -> ExportPlayersToDbUseCase:
    return ExportPlayersToDbUseCase(
        provide_GetPlayersAfterSkillsUpdateUseCase(),
        provide_PlayerRepository(),
    )


def provide_FilterOnPlayerNumbersUseCase() -> FilterOnPlayerNumbersUseCase:
    return FilterOnPlayerNumbersUseCase()


def provide_FilterOnInterestingPlayersUseCase() -> FilterOnInterestingPlayersUseCase:
    return FilterOnInterestingPlayersUseCase()
