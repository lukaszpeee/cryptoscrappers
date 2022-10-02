from functools import reduce
import pandas as pd


class MergedRaport:
    def __init__(self, raports_list, completed_raport_path: str):
        self.raports_list = raports_list
        self.completed_raport_path = completed_raport_path
        
    def merge_raports(self):
        completed_raport = reduce(lambda left, right: pd.merge(left, right, on=['Tag'], how='outer'), self.raports_list)
        return completed_raport
