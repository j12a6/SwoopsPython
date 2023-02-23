from enum import Enum


class ShortSkillName(Enum):
    THREE_POINT_SHOOTING = "3PT"
    INTERIOR_TWO_POINT_SHOOTING = "2PT-INT"
    MIDRANGE_TWO_POINT_SHOOTING = "2PT-MID"
    FREE_THROW = "FT"
    DEFENSIVE_REBOUND = "DREB"
    OFFENSIVE_REBOUND = "OREB"
    ASSIST = "PASS"
    INTERIOR_DEFENSE = "IDEF"
    PERIMETER_DEFENSE = "PDEF"
    PHYSICALITY = "PHY"
    LONGEVITY = "LONG"
    HUSTLE = "HSTL"
    BASKETBALL_IQ = "IQ"
    LEADERSHIP = "LDRS"
    COACHABILITY = "COACH"

    def __str__(self):
        return self.value

    @classmethod
    def to_values(cls):
        return [elem.value for elem in cls]
