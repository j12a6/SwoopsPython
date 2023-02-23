import os
import time
from pathlib import Path

import requests

from src.di.domain.DomainDi import provide_ExportPlayersToDbUseCase
from src.domain.SkillName import SkillName
from src.domain.model.Player import Player
from src.domain.model.SkillDetail import SkillDetail
from src.domain.usecase.ExportPlayersToDbUseCase import ExportPlayersToDbUseCase


# def make_request(players_path: str) -> None:
#     contract_address = "0xc211506d58861857c3158af449e832cc5e1e7e7b"
#     player_id = "1"
#     api_endpoint = f"https://api.opensea.io/api/v1/asset/{contract_address}/{player_id}/?include_orders=false"
#     response = requests.get(api_endpoint)
#     with open(f"{players_path}{player_id}.json", "w") as f:
#         f.write(response.text)


def filter_on_skill_scores(player: Player) -> bool:
    if player.skills.get(SkillName.THREE_POINT_SHOOTING, default_skill_detail()).score > 90:
        return True
    return False


def default_skill_detail() -> SkillDetail:
    return SkillDetail(score=0, revealed=False)


def save_new_games():
    directory = os.path.join(str(Path.home()), "Projects/databases/swoops/api/games/")
    for game_id in range(1901, 1901):
        print(game_id)
        api_endpoint = f"https://api.playswoops.com/api/game/{game_id}/"
        for i in range(0, 3):
            response = requests.get(api_endpoint)
            text = response.text
            if 'Bad Gateway' not in text:
                with open(f"{directory}{game_id}.json", "w") as f:
                    f.write(response.text)
                break
            time.sleep(3.17)
        time.sleep(1.22)


# if __name__ == '__main__':
#     use_case = provide_ExportPlayersToDbUseCase()
#     use_case.execute()
    # save_new_games()
