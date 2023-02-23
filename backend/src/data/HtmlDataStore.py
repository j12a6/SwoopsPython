import os
from typing import Iterable

from bs4 import BeautifulSoup
from lxml import etree

from src.data.PathProvider import PathProvider
from src.data.model.PlayerDto import PlayerDto


class HtmlDataStore:

    def __init__(self, path_provider: PathProvider):
        self.path_provider = path_provider

    def get_players(self) -> Iterable[PlayerDto]:
        player_ids = self.__get_player_ids()[:3]
        return iter(self.__get_player(player_id) for player_id in player_ids)

    def __get_player(self, player_id: str) -> PlayerDto:
        traits = self.__get_traits(player_id)
        return PlayerDto(number=player_id, traits=traits)

    def __get_player_ids(self) -> list[str]:
        dir_path = self.path_provider.get_players_html_dir_path()
        filenames = self.__get_filenames(dir_path)
        return list(map(self.__get_player_id_from_filename, filenames))

    def __get_traits(self, player_id: str) -> list[dict[str: object]]:
        dir_path = self.path_provider.get_players_html_dir_path()
        filename = self.path_provider.get_player_html_filename(player_id)
        file_path = f"{dir_path}{filename}"
        dom = self.__load_dom_from_html_file(file_path)
        return self.__get_traits_from_dom(dom)

    @staticmethod
    def __get_filenames(path: str) -> list[str]:
        return list(file for file in os.listdir(path) if file.endswith(".html"))

    @staticmethod
    def __get_player_id_from_filename(filename: str) -> str:
        return filename.replace("player_", "").replace(".html", "")

    @staticmethod
    def __load_dom_from_html_file(file_path):
        with (open(file_path, "r")) as f:
            html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')
            dom = etree.HTML(str(soup))
            return dom

    @staticmethod
    def __get_traits_from_dom(dom) -> list[dict[str: object]]:
        property_types = dom.xpath('//div[@class="Property--type"]/text()')
        property_values = dom.xpath('//div[@class="Property--value"]/text()')
        traits_dict = dict(zip(property_types, property_values))
        boost_types = dom.xpath('//h6[contains(@class,"Boost--label-trait-type")]/text()')
        boost_values = dom.xpath('//div[@data-progress]/@data-progress')
        traits_dict.update(dict(zip(boost_types, map(lambda x: float(x), boost_values))))
        numeric_types = dom.xpath('//div[@class="NumericTrait--type"]/text()')
        numeric_values = dom.xpath('//div[@class="NumericTrait--value"]/text()')[::2]
        traits_dict.update(dict(zip(numeric_types, map(lambda x: int(x), numeric_values))))
        traits_list = []
        for key, value in traits_dict.items():
            traits_list.append({"trait_type": key, "value": value})
        return traits_list
