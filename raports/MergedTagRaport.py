from functools import reduce
from typing import List

import pandas as pd
from pandas import DataFrame


class MergedTagRaport:
    def __init__(self, raports_list: List[DataFrame]):
        self.raports_list = raports_list
        
    def merge_raports(self) -> DataFrame:
        completed_raport = reduce(lambda left, right: pd.merge(left, right, on=['Tag'], how='outer'), self.raports_list)
        return completed_raport
