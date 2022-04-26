import pandas as pd

cashflow = pd.read_csv('PF_Pivot1.csv', delimiter=';')
print(cashflow.head(10))