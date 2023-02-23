from dataclasses import dataclass

from front.common.ShortSkillName import ShortSkillName
from front.common.SkillDetailUi import SkillDetailUi


@dataclass(frozen=True)
class PlayerUi:
    number: str
    prospect: int
    season: int
    position: str
    skills: dict[ShortSkillName: SkillDetailUi]
