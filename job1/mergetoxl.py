import pandas as pd

df1 = pd.read_csv("job1/data1.csv", index_col=0)
df2 = pd.read_csv("job1/data2.csv", index_col=0)
dftoxl = df1.append(df2, ignore_index=True)
dftoxl.to_excel("job1/combine.xlsx", sheet_name="Sheet1", index=False)
