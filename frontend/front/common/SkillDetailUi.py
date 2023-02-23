from dataclasses import dataclass

from src.domain.SkillRank import SkillRank


@dataclass(frozen=True)
class SkillDetailUi:
    score: float
    min_score: float
    max_score: float
    revealed: bool
    rank: SkillRank
    background_color: str
