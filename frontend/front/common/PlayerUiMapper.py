from front.common.PlayerUi import PlayerUi
from front.common.ShortSkillName import ShortSkillName
from front.common.SkillDetailUi import SkillDetailUi
from src.domain.SkillName import SkillName
from src.domain.SkillRank import SkillRank
from src.domain.model.Player import Player
from src.domain.model.SkillDetail import SkillDetail


class PlayerUiMapper:

    def __init__(self):
        pass

    def map(self, player: Player) -> PlayerUi:
        return PlayerUi(
            number=player.number,
            prospect=player.prospect,
            season=player.season,
            position="/".join(list(player.position)),
            skills=self.__get_skills(player.skills, player.top_skills),
        )

    def __get_skills(
            self,
            skills: dict[SkillName: SkillDetail],
            top_skills: dict[SkillRank: SkillName],
    ) -> dict[SkillName: SkillDetailUi]:
        return {
            self.__get_short_skill_name(skill_name): SkillDetailUi(
                score=round(skill.score, 1),
                min_score=round(skill.min_score, 1),
                max_score=round(skill.max_score, 1),
                revealed=skill.revealed,
                rank=self.__get_rank(skill_name, top_skills),
                background_color=self.__get_background_color(skill.score if skill.revealed else skill.min_score),
            )
            for skill_name, skill in skills.items()
        }

    @staticmethod
    def __get_rank(skill_name: SkillName, top_skills: dict[SkillRank: SkillName]) -> SkillRank:
        rank = [k for k, v in top_skills.items() if v == skill_name]
        return rank[0] if rank else SkillRank.OTHER

    @staticmethod
    def __get_background_color(score: float) -> str:
        if score > 95:
            return "#0f1f39"
        elif score > 90:
            return "#15294c"
        elif score > 85:
            return "#1a345f"
        elif score > 80:
            return "#1f3e73"
        elif score > 75:
            return "#254886"
        elif score > 70:
            return "#2a5399"
        elif score > 65:
            return "#2f5dac"
        else:
            return "#3568bf"


    @staticmethod
    def __get_short_skill_name(skill_name: SkillName) -> ShortSkillName:
        if skill_name == SkillName.THREE_POINT_SHOOTING:
            return ShortSkillName.THREE_POINT_SHOOTING
        elif skill_name == SkillName.INTERIOR_TWO_POINT_SHOOTING:
            return ShortSkillName.INTERIOR_TWO_POINT_SHOOTING
        elif skill_name == SkillName.MIDRANGE_TWO_POINT_SHOOTING:
            return ShortSkillName.MIDRANGE_TWO_POINT_SHOOTING
        elif skill_name == SkillName.FREE_THROW:
            return ShortSkillName.FREE_THROW
        elif skill_name == SkillName.DEFENSIVE_REBOUND:
            return ShortSkillName.DEFENSIVE_REBOUND
        elif skill_name == SkillName.OFFENSIVE_REBOUND:
            return ShortSkillName.OFFENSIVE_REBOUND
        elif skill_name == SkillName.ASSIST:
            return ShortSkillName.ASSIST
        elif skill_name == SkillName.INTERIOR_DEFENSE:
            return ShortSkillName.INTERIOR_DEFENSE
        elif skill_name == SkillName.PERIMETER_DEFENSE:
            return ShortSkillName.PERIMETER_DEFENSE
        elif skill_name == SkillName.PHYSICALITY:
            return ShortSkillName.PHYSICALITY
        elif skill_name == SkillName.LONGEVITY:
            return ShortSkillName.LONGEVITY
        elif skill_name == SkillName.HUSTLE:
            return ShortSkillName.HUSTLE
        elif skill_name == SkillName.BASKETBALL_IQ:
            return ShortSkillName.BASKETBALL_IQ
        elif skill_name == SkillName.LEADERSHIP:
            return ShortSkillName.LEADERSHIP
        elif skill_name == SkillName.COACHABILITY:
            return ShortSkillName.COACHABILITY
