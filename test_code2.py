from re import finditer
import pandas as pd

PATH = "C:/Users/vinay/Documents/BioUrja Renewables Attendance Tracker Build/sample.csv"

df = pd.read_csv(PATH)
df['Dependent_Table'] = pd.NaT

for ddl in df['DDL']:
    statement = f"""{ddl}"""
    lst = []
    table_lst = []
# from_tables = re.findall('POWERDB', statement)
# print(from_tables)
    for match in finditer('POWERDB', statement):
        initial_index = match.start()
        prune = str(statement[initial_index:initial_index+69])
        prune = (prune.split(' ', 1))
        lst.append(prune[0])
        print(lst)
        # for table in lst:
        #     table = str(table)
        #     table = table.split('\n', 1)
        #     table_lst.append(table[0])
        # print(table)