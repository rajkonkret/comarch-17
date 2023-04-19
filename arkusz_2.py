import pandas as pd

excel_data = pd.read_excel('sales.xlsx')

data = pd.DataFrame(excel_data)
print("Content\n", data)
data_2 = pd.DataFrame(excel_data, columns=["Sales Date", 'Sales Person', 'Amount'])
print(data_2)
