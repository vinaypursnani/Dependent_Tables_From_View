from re import finditer
import pandas as pd

PATH = "C:/Users/vinay/Documents/BioUrja Renewables Attendance Tracker Build/sample.csv"

df = pd.read_csv(PATH)
df['Dependent_Table'] = pd.NaT

for ddl in df['DDL']:
    statement = f"""{ddl}"""
    lst = []
# from_tables = re.findall('POWERDB', statement)
# print(from_tables)
    for match in finditer('POWERDB', statement):
        initial_index = match.start()
        prune = str(statement[initial_index:initial_index+69])
        xyz = prune.split(' ', 1)
        xyz = prune
        lst.append(xyz[0])
    df.append(new_row, ignore_index=True)
