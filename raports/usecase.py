from typing import List

from pandas import DataFrame

from data.raports import raport_01, raport_02, raport_03, raport_04, raport_05, raport_06, raport_07, raport_08, \
    raport_09, raport_10, raport_11
from raports.MergedTagRaport import MergedTagRaport

raports = [raport_01, raport_02, raport_03, raport_04, raport_05, raport_06, raport_07, raport_08, raport_09,
           raport_10, raport_11]


def main_mergedraport(raports_list: List[DataFrame], path: str) -> DataFrame:

    merged_raport = MergedTagRaport(raports_list, f'{path}/completed_raport.xlsx')
    result = merged_raport.merge_raports()
    result.to_excel(merged_raport.completed_raport_path)

