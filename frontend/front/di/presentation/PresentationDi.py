from front.presentation.SearchViewModel import SearchViewModel
from src.di.domain.DomainDi import provide_GetPlayersUseCase
from src.di.domain.DomainDi import provide_FilterOnInterestingPlayersUseCase
from src.di.domain.DomainDi import provide_FilterOnPlayerNumbersUseCase


def provide_SearchViewModel() -> SearchViewModel:
    return SearchViewModel(
        provide_GetPlayersUseCase(),
        provide_FilterOnPlayerNumbersUseCase(),
        provide_FilterOnInterestingPlayersUseCase(),
    )
