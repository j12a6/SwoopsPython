from typing import Iterable

from src.domain.SkillName import SkillName
from src.domain.model import Player


class FilterOnInterestingPlayersUseCase:

    def execute(self, players: Iterable[type[Player]]) -> Iterable[type[Player]]:
        return filter(self.__filter_interesting, players)

    @staticmethod
    def __filter_interesting(player: Player) -> bool:
        criterias = [
            (SkillName.COACHABILITY, ScoreComparator.MAX_SCORE_MORE_THAN, 40),
        ]
        # test = [f"{_} - {skill}" for _, skill in player.skills.items() if Hey.MAX_SCORE_MORE_THAN(skill, 70)]
        return test(player)
        # return is_good_now(player) or will_evolve_soon(player)
        # for skill_name, value in criterias:
        #     print(f"{player.number}  -  {player.skills[skill_name].max_score}")
        #     if player.skills[skill_name].max_score < value:
        #         return False


def test(player: Player):
    condition_1 = len(
        ["" for skill in player.skills.values() if ScoreComparator.MIN_SCORE_MORE_THAN(skill, 90)]
    ) == 1
    # condition_2 = len(
    #     ["" for skill in player.skills.values() if ScoreComparator.MIN_SCORE_MORE_THAN(skill, 90)]
    # ) >= 2
    return condition_1

def is_good_now(player: Player):
    condition_1 = len(
        ["" for skill in player.skills.values() if ScoreComparator.MIN_SCORE_MORE_THAN(skill, 80)]
    ) >= 3
    condition_2 = len(
        ["" for skill in player.skills.values() if ScoreComparator.MIN_SCORE_MORE_THAN(skill, 90)]
    ) >= 2
    return condition_1 or condition_2


def will_evolve_soon(player: Player):
    condition_1 = ScoreComparator.MIN_SCORE_MORE_THAN(player.skills[SkillName.COACHABILITY], 80)
    condition_2 = len(
        ["" for skill_name, skill in player.skills.items() if
         ScoreComparator.MIN_SCORE_MORE_THAN(skill, 65) and skill_name is not SkillName.COACHABILITY]
    ) >= 1
    return condition_1 and condition_2


from enum import Enum


class ScoreComparator(Enum):
    MIN_SCORE_MORE_THAN = lambda x, y: x.min_score > y
    MIN_SCORE_LESS_THAN = lambda x, y: x.min_score < y
    MAX_SCORE_MORE_THAN = lambda x, y: x.max_score > y
    MAX_SCORE_LESS_THAN = lambda x, y: x.max_score > y
