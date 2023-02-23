import random

import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'swoopsspider'
    allowed_domains = ['opensea.io']
    custom_settings = {
        'DOWNLOAD_DELAY': random.randint(6, 32),
    }

    def start_requests(self):
        base_url = f"https://opensea.io/assets/ethereum/0xc211506d58861857c3158af449e832cc5e1e7e7b/"
        for i in range(196, 1501):
            headers = self.get_headers()
            yield scrapy.Request(
                url=base_url + str(i),
                method='GET',
                headers=headers,
                callback=self.parse,
            )

    def parse(self, response, **kwargs):
        player_id = response.url.split("/")[-1]
        with open(f"players/player_{player_id}.html", 'wb') as f:
            f.write(response.body)
        yield response.body

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
