from raports.MergedRaport import MergedRaport


class VerificationMergedRaport:
    
    def __init__(self, merged_raport: MergedRaport):
        self.merged_raport = merged_raport
        
    def check_first_and_last_month(self):
        checked_rows = []
        number_of_columns = len(self.merged_raport.columns)
        for i, row in self.merged_raport.iterrows():
            if row['Styczeń'] < row['Sierpień']:
                checked_rows.append(True)
            else:
                checked_rows.append(False)
        self.merged_raport['First_and_last'] = checked_rows
        return self.merged_raport
    
    def check_first_three_months(self):
        checked_rows = []
        for i, row in self.merged_raport.iterrows():
            if row['Styczeń'] < row['Luty'] < row['Marzec']:
                checked_rows.append(True)
            else:
                checked_rows.append(False)
        self.merged_raport['First_three_months'] = checked_rows
        return self.merged_raport
    
    def check_last_three_months(self):
        checked_rows = []
        number_of_columns = len(self.merged_raport.columns)
        for i, row in self.merged_raport.iterrows():
            if row['Czerwiec'] < row['Lipiec'] < row['Sierpień']:
                checked_rows.append(True)
            else:
                checked_rows.append(False)
        self.merged_raport['Last_free'] = checked_rows
        return self.merged_raport
    
    def check_all_months(self):
        checked_rows = []
        number_of_columns = len(self.merged_raport.columns)
        for i, row in self.merged_raport.iterrows():
            if row['Styczeń'] < row['Luty'] < row['Marzec'] < row['Kwiecień'] < row['Maj'] < row['Czerwiec'] < row['Lipiec'] < row['Sierpień']:
                checked_rows.append(True)
            else:
                checked_rows.append(False)
        self.merged_raport['All_months'] = checked_rows
        return self.merged_raport