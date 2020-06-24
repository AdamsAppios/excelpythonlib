import xlwings as xw
import pandas as pd


def freezeWhat(wb, row, col):
    wb = xw.books.active
    active_window = wb.app.api.ActiveWindow
    active_window.FreezePanes = False
    active_window.SplitColumn = col
    active_window.SplitRow = row
    active_window.FreezePanes = True


def xltodf(sheetobject, a1string):
    return sheetobject.range(a1string).options(pd.DataFrame, expand='table').value
