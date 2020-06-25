# https://www.toogit.com/proposals/create/need-to-marry-information-onto-1-spreadsheet
import xlwings as xw
from xlwings.utils import rgb_to_int
import pandas as pd
import numpy as np
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
current_directory = "\\".join(dir_path.split("\\"))
df1 = pd.read_csv(os.path.join(current_directory, "data1.csv"))
df2 = pd.read_csv(os.path.join(current_directory, "data2.csv"))
common = df1.merge(df2, on=['Order#', 'Cost'])
highlight = df2[(~df2["Order#"].isin(common["Order#"]))].index.values
newhighlight = ["A"+str(i+2) for i in highlight]
a1notation = ",".join(newhighlight)
df2.to_excel(os.path.join(current_directory, "df2.xlsx"),
             sheet_name="df2", index=False)
sht = xw.Book(os.path.join(current_directory, "df2.xlsx")).sheets["df2"]
sht.range(a1notation).api.Font.Color = rgb_to_int((205, 92, 92))
