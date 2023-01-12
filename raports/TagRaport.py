from typing import List
import pandas as pd
from pandas import DataFrame


class TagRaport:
    def __init__(self, month: str, scrapper_data: List[str]):
        self.month = month
        self.scrapper_data = scrapper_data
        
    def create_tag_raport(self) -> DataFrame:
        df_tags = pd.DataFrame(self.scrapper_data, columns=['Tag'])
        df_counted_tags = df_tags.groupby(['Tag'])['Tag'].count().sort_values(ascending=False)
        df_counted_tags = pd.DataFrame(df_counted_tags, columns=['Tag'])
        df_counted_tags = df_counted_tags.rename(columns={'Tag': self.month})
        return df_counted_tags
