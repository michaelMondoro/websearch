from bs4 import BeautifulSoup
import requests 
from page import * 
import logging
from datetime import datetime

logging.basicConfig(
        level=logging.INFO,             
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

class SearchEngine:
    HEADERS = headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/122.0 Safari/537.36"
    }
    BASE_URL = "https://html.duckduckgo.com/html/"
    TIMEFRAMES = ['d', 'w', 'm', 'y']

    def __init__(self, logs:bool=True):
        self.results = []
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.disabled = not logs

    def search(self, query:str, count:int=10, timeframe:str=''):
        params = {
            'q': query,
            'df': timeframe if timeframe in SearchEngine.TIMEFRAMES else ''
        }

        res = requests.post(SearchEngine.BASE_URL, data=params, headers=SearchEngine.HEADERS)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        
        for i, result in enumerate(soup.select(".result")):
            if i == count: break
            a_tag = result.find("a", class_="result__a")
            href = a_tag.get("href")
            self.logger.info(f"Processing web result: {href}")
            extras = result.find("div", class_="result__extras__url")
            date_span = extras.find("span", class_=lambda c: not c)
            date =  datetime.fromisoformat(date_span.text.strip().split(".")[0]) if date_span is not None else None

            self.results.append(SimpleWebpage(href, date))

        return self.results
    
    def __str__(self):
        return (
            f"Engine(results={len(self.results)}, "
            f"logging={'enabled' if not self.logger.disabled else 'disabled'})"
        )
    def __repr__(self):
        return (
            f"Engine(results={len(self.results)}, "
            f"logging={'enabled' if not self.logger.disabled else 'disabled'})"
        )
