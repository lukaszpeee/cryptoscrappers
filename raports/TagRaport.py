from typing import List
import pandas as pd
from pandas import DataFrame


class TagRaport:
    def __init__(self, month: str, scrapper_data: List, raport_path: str):
        self.month = month
        self.scrapper_data = [x.upper() for x in scrapper_data]
        self.raport_path = raport_path
        
    def create_tag_raport(self) -> DataFrame:
        df_tags = pd.DataFrame(self.scrapper_data, columns=['Tag'])
        df_counted_tags = df_tags.groupby(['Tag'])['Tag'].count().sort_values(ascending=False)
        df_counted_tags = pd.DataFrame(df_counted_tags, columns=['Tag'])
        df_counted_tags = df_counted_tags.rename(columns={'Tag': self.month})
        df_counted_tags.to_excel(self.raport_path)
