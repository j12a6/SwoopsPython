from front.common.PlayerUiMapper import PlayerUiMapper
from src.domain.usecase.FilterOnInterestingPlayersUseCase import FilterOnInterestingPlayersUseCase
from src.domain.usecase.FilterOnPlayerNumbersUseCase import FilterOnPlayerNumbersUseCase
from src.domain.usecase.GetPlayersUseCase import GetPlayersUseCase


class SearchViewModel:

    def __init__(
            self,
            get_players_use_case: GetPlayersUseCase,
            filter_on_player_numbers_use_case: FilterOnPlayerNumbersUseCase,
            filter_on_interesting_players_use_case: FilterOnInterestingPlayersUseCase,
    ):
        self.get_players_use_case = get_players_use_case
        self.filter_on_player_numbers_use_case = filter_on_player_numbers_use_case
        self.filter_on_interesting_players_use_case = filter_on_interesting_players_use_case

    def start(self):
        players = self.get_players_use_case.execute()

        player_numbers = [
            "66", "584", "585", "844",
            "580", "581", "685",
            "582", "583", "847",
            # "802", "724", "456", "505", "1223", "554", "553", "441", "81", "284", "1151", "495",
            # "1216", "94", "1402", "1372", "1219", "1296", "762", "403", "1323", "726", "506",
            # "443", "822", "803", "124", "999", "92", "1411", "712", "527", "1230", "681", "740", "1498", "543",
            # "934", "1111", "1014"
        ]

        players = self.filter_on_player_numbers_use_case.execute(players, player_numbers)
        # players = self.filter_on_interesting_players_use_case.execute(players)

        # players = PlayerAsDictUseCase().execute(players)
        # players = [player for player in players if
        #            player[Skill.COACHABILITY.value] > 80
        #            and player[Skill.LONGEVITY.value] > 80
        #            and any(score > 80 for skill, score in player.items() if isinstance(score, float))]

        mapper_ui = PlayerUiMapper()
        players_ui = map(mapper_ui.map, players)

        players_ui = sorted(players_ui, key=lambda player: int(player.number))
        return players_ui
