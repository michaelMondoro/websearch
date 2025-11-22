
from requests import get
from dataclasses import dataclass, field
from bs4 import BeautifulSoup
from datetime import datetime

@dataclass
class Sentiment:
    pos: float
    neg: float
    neutral: float
    label: str = field(init=False)
    value: float = field(init=False)

    def __post_init__(self):
        scores = {
            'positive': self.pos,
            'negative': self.neg,
            'neutral': self.neutral
        }
        self.label, self.value = max(scores.items(), key=lambda item: item[1])
    


class SimpleWebpage:
    HEADERS = headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/122.0 Safari/537.36"
    }
    def __init__(self, url:str, date:datetime):
        self.url = url
        self.status = None
        self.text = None
        self.title = None
        self.links = []
        self.sentiment = None
        self.date = date
        self._load()
    
    def _load(self):
        response = get(self.url, headers=SimpleWebpage.HEADERS)
        self.status = response.status_code
        if self.status != 200: 
            print(f"ERROR: {response.content}")
            return
        soup = BeautifulSoup(response.content, 'html.parser')
        # title
        title = soup.find("title")
        if title: self.title = title.text

        # text
        body = soup.find("body")
        p_tags = body.find_all("p")
        self.text = " ".join(p.text for p in p_tags)

        # links 
        self.links = soup.find_all('a', href=True)
        

    def __str__(self):
        return f"SimpleWebpage(url={self.url}, title={self.title}, date={self.date.strftime('%Y-%m-%d')}, status={self.status}, text={self.text[:25] if self.text else ""}...)"

    def __repr__(self):
        return f"SimpleWebpage(url={self.url}, title={self.title}, date={self.date.strftime('%Y-%m-%d')}, status={self.status}, text={self.text[:25]if self.text else ""}...)"