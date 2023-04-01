from typing import List
import pandas as pd
from pandas import DataFrame


class TagRaport:
    def __init__(self, month: str, scrapper_data: List[str]):
        self._month = month
        self._scrapper_data = scrapper_data
        
    def create_tag_raport(self) -> DataFrame:
        df_tags = pd.DataFrame(self._scrapper_data, columns=[self._month])
        df_counted_tags = df_tags.groupby([self._month])[self._month].count().sort_values(ascending=False)
        df_tag_raport = pd.DataFrame({'TAG': df_counted_tags.index, self._month: df_counted_tags.values})
        return df_tag_raport
