from typing import List
from functools import reduce
from raports.ScrapperProfilesRaport import ScrapperProfilesRaport
import pandas as pd


class CompletedScapperProfilesRaport:
    
    def __init__(self, raports_list: List[ScrapperProfilesRaport], completed_raport_path: str):
        self.raports_list = raports_list
        self.completed_raport_path = completed_raport_path
        
    def merge_raports(self):
        completed_raport = reduce(lambda x, y: pd.merge(x, y, on = 'Tag'), self.raports_list)
        completed_raport.to_excel(self.completed_raport_path)
    
    