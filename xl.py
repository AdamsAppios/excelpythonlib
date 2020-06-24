import xlwings as xw
import datetime as dt
import pandas as pd
from xlwingsfunctions.basicfunctions import *
import numpy as np
sht = xw.Book("sample.xlsx").sheets[0]
autofitColumn(sht)
