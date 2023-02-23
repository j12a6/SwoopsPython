from dataclasses import dataclass


@dataclass(frozen=True)
class SkillDetail:
    score: float
    min_score: float
    max_score: float
    revealed: bool

    def copy(
            self,
            score: float = None,
            min_score: float = None,
            max_score: float = None,
            revealed: bool = None
    ):
        return SkillDetail(
            score if score is not None else self.score,
            min_score if min_score is not None else self.min_score,
            max_score if max_score is not None else self.max_score,
            revealed if revealed is not None else self.revealed,
        )
