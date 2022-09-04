from raports.MergedRaport import MergedRaport
from abc import ABC, abstractmethod


class Verification(ABC):
    @abstractmethod
    def make_verivication(self, row, checked_rows, ver_name: str):
        pass
    
class VeriticationFirstAndLast(Verification):
    ver_name: str = 'First_and_last'

    def __init__(self, merged_raport):
        self.merged_raport = merged_raport
    
    def make_verivication(self):
        checked_rows = []
        number_of_columns = len(self.merged_raport.columns)
        for i, row in self.merged_raport.iterrows():
            if row['Styczeń'] < row['Sierpień']:
                checked_rows.append(True)
            else:
                checked_rows.append(False)
        self.merged_raport[VeriticationFirstAndLast.ver_name] = checked_rows
        return self.merged_raport
    
class VeriticationFirstThreeMonths(Verification):
    ver_name: str = 'First_three_months'
    
    def __init__(self, merged_raport):
        self.merged_raport = merged_raport
    
    def make_verivication(self):
        checked_rows = []
        for i, row in self.merged_raport.iterrows():
            if row['Styczeń'] < row['Luty'] < row['Marzec']:
                checked_rows.append(True)
            else:
                checked_rows.append(False)
        self.merged_raport[VeriticationFirstThreeMonths.ver_name] = checked_rows
        return self.merged_raport
        
class VeriticationLastFreeMonths(Verification):
    ver_name: str = 'Last_three_months'
    
    def __init__(self, merged_raport):
        self.merged_raport = merged_raport
    
    def make_verivication(self):
        checked_rows = []
        number_of_columns = len(self.merged_raport.columns)
        for i, row in self.merged_raport.iterrows():
            if row['Czerwiec'] < row['Lipiec'] < row['Sierpień']:
                checked_rows.append(True)
            else:
                checked_rows.append(False)
        self.merged_raport[VeriticationLastFreeMonths.ver_name] = checked_rows
        return self.merged_raport
        
class VeriticationAllMonths(Verification):
    ver_name: str = 'All_months'
    
    def __init__(self, merged_raport):
        self.merged_raport = merged_raport
      
    def make_verivication(self):
        checked_rows = []
        number_of_columns = len(self.merged_raport.columns)
        for i, row in self.merged_raport.iterrows():
            if row['Styczeń'] < row['Luty'] < row['Marzec'] < row['Kwiecień'] < row['Maj'] < row['Czerwiec'] < row['Lipiec'] < row['Sierpień']:
                checked_rows.append(True)
            else:
                checked_rows.append(False)
        self.merged_raport[VeriticationAllMonths.ver_name] = checked_rows
        return self.merged_raport