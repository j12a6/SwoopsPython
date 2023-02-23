import logging
import os
import random

import scrapy
from scrapy.http import HtmlResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# response.xpath('//div[@class="Property--type"]/text()').extract()
# response.xpath('//div[@class="Property--value"]/text()').extract()

# response.xpath('//h6[contains(@class,"Boost--label-trait-type")]/text()').extract()
# response.xpath('//div[@data-progress]/@data-progress').extract()

class ExampleSpider(scrapy.Spider):
    name = 'swoops_from_file_spider'
    allowed_domains = "127.0.0.1"
    custom_settings = {
        'DOWNLOAD_DELAY': 0,
    }

    def start_requests(self):
        html_dir_name = "players"
        file_prefix = "player_"
        player_id = 1
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = f"{BASE_DIR}/{html_dir_name}/{file_prefix}{player_id}.html"
        uri = f"file://127.0.0.1{filename}"
        with open(filename, "r") as f:
            file_content = f.read()
            yield HtmlResponse(url=uri, body=file_content, encoding="utf-8")
            # for i in range(1, 2):
            # yield scrapy.Request(
            #     url=f"file:///{path}{file_prefix}{str(i)}.html",
            #     callback=self.parse,
            # )

    def parse(self, response, **kwargs):
        player_id = response.url.split("/")[-1].replace("player_", "").replace(".html", "")
        print(f"player_id={player_id}")
        logging.debug(f"player_id={player_id}")
        yield "a"

    @staticmethod
    def get_headers():
        return {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "DNT": "1",
            "Host": "opensea.io",
            "Referer": "https://opensea.io/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        }
