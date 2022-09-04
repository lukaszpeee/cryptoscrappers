from functools import reduce
import pandas as pd


class MergedRaport:
    
    def __init__(self, raports_list, completed_raport_path: str):
        self.raports_list = raports_list
        self.completed_raport_path = completed_raport_path
        
    def merge_raports(self, merge_on: str):
        completed_raport = reduce(lambda x, y: pd.merge(x, y, on = merge_on), self.raports_list)
        return completed_raport