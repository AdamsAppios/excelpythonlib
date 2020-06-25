import xlwings as xw
import datetime as dt
import pandas as pd
from xlwingsfunctions.basicfunctions import *
from pandasfunctions.pandastringmanip import *
import numpy as np
dummy_data1 = {
    'id': ['1', '2', '3', '4', '5'],
    'Feature1': ['A', 'C', 'E', 'G', 'I'],
    'Feature2': ['B', 'D', 'F', 'H', 'J']}
df1 = pd.DataFrame(dummy_data1, columns=['id', 'Feature1', 'Feature2'])
dummy_data2 = {
    'id': ['1', '2', '6', '7', '8'],
    'Feature1': ['K', 'M', 'O', 'Q', 'S'],
    'Feature2': ['L', 'N', 'P', 'R', 'T']}
df2 = pd.DataFrame(dummy_data2, columns=['id', 'Feature1', 'Feature2'])
dummy_data3 = {
    'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'Feature3': [12, 13, 14, 15, 16, 17, 15, 12, 13, 23]}
df3 = pd.DataFrame(dummy_data3, columns=['id', 'Feature3'])
frames = [df1, df2]
df_keys = pd.concat(frames, keys=['x', 'y'])
print(df_keys)
