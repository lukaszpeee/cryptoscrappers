from functools import reduce
from typing import List

import pandas as pd
from pandas import DataFrame


class MergedTagRaport:
    def __init__(self, raports_list: List[DataFrame]):
        self._raports_list = raports_list

    def create_merged_tag_raport(self, path: str, name: str) -> DataFrame:
        merged_df_tag_raports = reduce(lambda left, right: pd.merge(left, right, on=['TAG'], how='outer'),
                                       self._raports_list)
        merged_df_tag_raports.to_excel(f"{path}/{name}.xlsx", index=False)
