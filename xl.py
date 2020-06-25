import xlwings as xw
from xlwings.utils import rgb_to_int
import datetime as dt
import pandas as pd
from xlwingsfunctions.basicfunctions import *
from pandasfunctions.pandastringmanip import *
import numpy as np

# creating a dataframe
sht = xw.Book("sample.xlsx").sheets["Sheet1"]
sht.range("A2,A5").api.Font.Color = rgb_to_int((205, 92, 92))
