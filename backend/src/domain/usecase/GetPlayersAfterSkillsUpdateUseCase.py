from itertools import pairwise
from typing import Iterable

from src.domain.SkillName import SkillName
from src.domain.SkillRank import SkillRank
from src.domain.model import Player
from src.domain.model.SkillDetail import SkillDetail


class GetPlayersAfterSkillsUpdateUseCase:

    def __init__(self):
        pass

    def execute(self, players: Iterable[type[Player]]) -> Iterable[type[Player]]:
        return [self.__update_player_skills(player) for player in players]

    def __update_player_skills(self, player: Player):
        not_top_skills = self.__get_skills_without_top_skills(player.skills, player.top_skills)
        highest_visible_score_skill_name = max(not_top_skills, key=lambda skill_name: not_top_skills[skill_name].score)
        self.__update_min_scores_of_top_skills(
            player.skills,
            player.top_skills[SkillRank.TOP_1],
            player.top_skills[SkillRank.TOP_2],
            player.top_skills[SkillRank.TOP_3],
            highest_visible_score_skill_name,
        )
        self.__update_max_scores_of_top_skills(
            player.skills,
            player.top_skills[SkillRank.TOP_1],
            player.top_skills[SkillRank.TOP_2],
            player.top_skills[SkillRank.TOP_3],
        )
        self.__update_max_scores(player.skills, player.top_skills)
        return player

    @staticmethod
    def __get_skills_without_top_skills(
            skills: dict[SkillName: SkillDetail],
            top_skills: dict[SkillRank: SkillName]
    ) -> dict[str: SkillDetail]:
        return {skill_name: skill for skill_name, skill in skills.items() if skill_name not in top_skills.values()}

    def __update_min_scores_of_top_skills(
            self,
            skills: dict[SkillName: SkillDetail],
            top_1_skill_name: SkillName,
            top_2_skill_name: SkillName,
            top_3_skill_name: SkillName,
            highest_visible_score_skill_name: SkillName,
    ) -> None:
        for to_copy_from, to_update in pairwise(
                [highest_visible_score_skill_name, top_3_skill_name, top_2_skill_name, top_1_skill_name]
        ):
            if not skills[to_update].revealed:
                skills[to_update] = skills[to_update].copy(
                    min_score=self.__get_score_or_min_score(skills[to_copy_from]),
                )

    def __update_max_scores_of_top_skills(
            self,
            skills: dict[SkillName: SkillDetail],
            top_1_skill_name: SkillName,
            top_2_skill_name: SkillName,
            top_3_skill_name: SkillName,
    ) -> None:
        for to_copy_from, to_update in pairwise(
                [top_1_skill_name, top_2_skill_name, top_3_skill_name]
        ):
            if not skills[to_update].revealed:
                skills[to_update] = skills[to_update].copy(
                    max_score=self.__get_score_or_max_score(skills[to_copy_from]),
                )

    def __update_max_scores(
            self,
            skills: dict[SkillName: SkillDetail],
            top_skills: dict[SkillRank: SkillName]
    ) -> None:
        for skill_name, skill in skills.items():
            if not skill.revealed and skill_name not in top_skills.values():
                skills[skill_name] = skill.copy(
                    max_score=self.__get_score_or_max_score(skills[top_skills[SkillRank.TOP_3]]),
                )

    @staticmethod
    def __get_score_or_min_score(skill: SkillDetail) -> float:
        return skill.score if skill.revealed else skill.min_score

    @staticmethod
    def __get_score_or_max_score(skill: SkillDetail) -> float:
        return skill.score if skill.revealed else skill.max_score
