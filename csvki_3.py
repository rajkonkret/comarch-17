import pandas as pd
import openpyxl
# pip install pandas

data = pd.read_csv('records.csv')
print(data)
print(data.columns)
col_names = data.columns.tolist()
print(col_names)
data.to_excel('records.xlsx', index=False)

# 13:30