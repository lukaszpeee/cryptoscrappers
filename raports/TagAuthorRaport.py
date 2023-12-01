from collections import Counter
from typing import List, Dict
import pandas as pd
from pandas import DataFrame


class TagAuthorRaport:
    def __init__(self, month: str, scrapper_data: List[Dict]):
        self._month = month
        self._scrapper_data = scrapper_data

    def create_tag_author_raport(self) -> DataFrame:
        counted_data = []
        grouped_list_of_author_tag_dicts = [{key: count} for key, count in Counter(
            [list(dict.values())[0] for dict in self._scrapper_data]).items()]
        for d in grouped_list_of_author_tag_dicts:
            for key, value in d.items():
                counted_data.append({'TAG': key, 'AUTHORS': value})
        return pd.DataFrame(counted_data)
