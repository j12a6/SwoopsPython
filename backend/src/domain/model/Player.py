from dataclasses import dataclass

from src.domain.SkillName import SkillName
from src.domain.SkillRank import SkillRank
from src.domain.model.SkillDetail import SkillDetail


@dataclass(frozen=True)
class Player:
    number: str
    prospect: int
    season: int
    position: str
    skills: dict[SkillName: SkillDetail]
    top_skills: dict[SkillRank: SkillName]
