from typing import List
import pandas as pd


class Raport:
    
    def __init__(self, month: str, crypto_tags: List, raport_path: str):
        self.month = month
        self.crypto_tags = crypto_tags
        self.raport_path = raport_path
        
    def create_scrapper_profiles_raport(self):
        tags = [tag.upper() for tag in self.crypto_tags]
        df_tags = pd.DataFrame(tags, columns=['Tag'])
        df_counted_tags = df_tags.groupby(['Tag'])['Tag'].count().sort_values(ascending=False)
        df_counted_tags = pd.DataFrame(df_counted_tags, columns=['Tag'])
        df_counted_tags = df_counted_tags.rename(columns={'Tag': self.month})
        df_counted_tags.to_excel(self.raport_path)