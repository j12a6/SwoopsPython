from enum import Enum


class Trait(Enum):
    PROSPECT = "Prospect"
    SEASON = "Season"
    POSITION_1 = "Position 1"
    POSITION_2 = "Position 2"
    TOP_1_SKILL = "1 Top Skill"
    TOP_2_SKILL = "2 Top Skill"
    TOP_3_SKILL = "3 Top Skill"

    def __str__(self):
        return self.value
