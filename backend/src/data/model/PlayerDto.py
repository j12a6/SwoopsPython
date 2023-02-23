from dataclasses import dataclass


@dataclass(frozen=True)
class PlayerDto:
    number: str
    traits: list[dict[str: object]]
