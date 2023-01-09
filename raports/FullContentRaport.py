from typing import List

import pandas as pd
from pandas import DataFrame


class FullContentRaport:
    def __init__(self, month: str, scrapper_data: List[str], raport_path: str):
        self.month = month
        self.scrapper_data = scrapper_data
        self.raport_path = raport_path

    def create_full_content_raport(self) -> DataFrame:
        df_content = pd.DataFrame(self.scrapper_data, columns=['Date', 'User', 'Tweet', 'Tags'])
        df_content['Date'] = df_content['Date'].apply(lambda a: pd.to_datetime(a).date())
        df_content.to_excel(self.raport_path)
