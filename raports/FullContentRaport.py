from typing import List

import pandas as pd
from pandas import DataFrame


class FullContentRaport:
    def __init__(self, scrapper_data: List[str]):
        self._scrapper_data = scrapper_data

    def create_full_content_raport(self) -> DataFrame:
        df_full_content_raport = pd.DataFrame(self._scrapper_data, columns=['Date', 'User', 'Tweet', 'Tags'])
        df_full_content_raport['Date'] = df_full_content_raport['Date'].apply(lambda a: pd.to_datetime(a).date())
        return df_full_content_raport
