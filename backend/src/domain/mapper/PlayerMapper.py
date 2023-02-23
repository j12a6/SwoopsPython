from src.data.model.PlayerDto import PlayerDto
from src.domain.SkillName import SkillName
from src.domain.SkillRank import SkillRank
from src.domain.Trait import Trait
from src.domain.model.Player import Player
from src.domain.model.SkillDetail import SkillDetail

MIN_SCORE = 30
MAX_SCORE = 100


class PlayerMapper:

    def map(self, player_dto: PlayerDto) -> Player:
        traits_dict = {}
        for trait in player_dto.traits:
            traits_dict[trait["trait_type"]] = trait["value"]
        return Player(
            number=player_dto.number,
            prospect=traits_dict[Trait.PROSPECT.value],
            season=traits_dict[Trait.SEASON.value],
            position=traits_dict[Trait.POSITION_1.value] + traits_dict.get(Trait.POSITION_2.value, ""),
            skills=self.__get_skills(traits_dict),
            top_skills={
                skill_rank: SkillName(self.__fix_wrong_naming_of_top_attributes(traits_dict[trait_rank.value]))
                for skill_rank, trait_rank in [
                    (SkillRank.TOP_1, Trait.TOP_1_SKILL),
                    (SkillRank.TOP_2, Trait.TOP_2_SKILL),
                    (SkillRank.TOP_3, Trait.TOP_3_SKILL),
                ]
            },
        )

    @staticmethod
    def __fix_wrong_naming_of_top_attributes(top_skill_name: str) -> str:
        if top_skill_name == "Free Throw Shooting":
            return "Free Throw"
        elif top_skill_name == "Passing":
            return "Assist"
        return top_skill_name

    @staticmethod
    def __get_skills(traits_dict: dict):
        skills = {
            skill_name: SkillDetail(
                score=0,
                min_score=MIN_SCORE,
                max_score=MAX_SCORE,
                revealed=False,
            ) for skill_name in SkillName
        }
        skills.update(
            {
                SkillName(k): SkillDetail(
                    score=v,
                    min_score=v if v > 0 else MIN_SCORE,
                    max_score=v if v > 0 else MAX_SCORE,
                    revealed=v > 0,
                )
                for k, v in traits_dict.items() if k in SkillName.to_values()
            }
        )
        return skills
