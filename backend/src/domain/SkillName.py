from enum import Enum


class SkillName(Enum):
    THREE_POINT_SHOOTING = "Three Point Shooting"
    INTERIOR_TWO_POINT_SHOOTING = "Interior Two Point Shooting"
    MIDRANGE_TWO_POINT_SHOOTING = "Midrange Two Point Shooting"
    FREE_THROW = "Free Throw"
    DEFENSIVE_REBOUND = "Defensive Rebound"
    OFFENSIVE_REBOUND = "Offensive Rebound"
    ASSIST = "Assist"
    INTERIOR_DEFENSE = "Interior Defense"
    PERIMETER_DEFENSE = "Perimeter Defense"
    PHYSICALITY = "Physicality"
    LONGEVITY = "Longevity"
    HUSTLE = "Hustle"
    BASKETBALL_IQ = "Basketball IQ"
    LEADERSHIP = "Leadership"
    COACHABILITY = "Coachability"

    def __str__(self):
        return self.value

    @classmethod
    def to_values(cls):
        return [elem.value for elem in cls]
