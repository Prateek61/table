import requests
import validators
import sys
import csv
from bs4 import BeautifulSoup

from typing import List, Dict, Iterable, Optional, Mapping, Any

class Extract:
    @classmethod
    def dict_to_csv(cls, rows: Iterable[Mapping[Any, Any]], file_name: Optional[str] = 'output.csv') -> None:
        with open(file_name, 'w') as file:
            for row in rows:
                writer = csv.DictWriter(file, fieldnames=row.keys())
                break
            writer.writerows(rows)

class ExtractUrl(Extract):
    def __init__(self, url: str):
        self.add_url(url)

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url: str):
        if not validators.url(url):
            raise ValueError("Invalid url")
        self._url = url

    def add_url(self, url: str):
        self.url = url

    @classmethod
    def run(cls, url: Optional[str] = None):
        if url:
            cls.url = url

        if not cls.url:
            raise ValueError("Url not provided")

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        html_tables = soup.find_all('table')

        for html_table in html_tables:
            dict_table = cls.dict_from_html_table(html_table)
            cls.dict_to_csv(dict_table)

    @classmethod
    def dict_from_html_table(cls, table: BeautifulSoup) -> List[dict]:
        html_table_rows = table.find_all('tr')
        to_return: List[dict] = list()
        table_heads: List[str] = list()

        for i, html_table_row in enumerate(html_table_rows):
            if i == 0:
                html_table_row_col_heads = html_table_row.find_all('th')
                if not html_table_row_col_heads:
                    print("No heads")
                    sys.exit(2)
                
                table_heads = cls.get_heads(html_table_row_col_heads)
            else:
                html_table_row_cols = html_table_row.find_all('td')
                to_return.append(cls.get_data_dict(table_heads ,html_table_row_cols))

        return to_return

    @classmethod
    def get_heads(cls, cols: Iterable[BeautifulSoup]) -> List[str]:
        heads: List[str] = list()

        for col in cols:
            heads.append(col.string)
        return heads

    @classmethod
    def get_data_dict(cls, heads: List[str], cols: Iterable[BeautifulSoup]) -> Dict[str, str]:
        to_return: Dict[str, str] = dict()

        for i, col in enumerate(cols):
            to_return[heads[i]] = col.string
        
        return to_return
