import xlwings as xw
import datetime as dt
import pandas as pd
from xlwingsfunctions.basicfunctions import *
from pandasfunctions.pandastringmanip import *
import numpy as np
sht = xw.books['sample.xlsx'].sheets["Sheet1"]
df = expandTable(sht, "A1", pd.DataFrame)
df['result'] = replaceLeftRight(df['result'], "+-", "aAbBcC")
print(df)
