
import pandas as pd


def replaceLeftRight(dfcol, left, right):
    return dfcol.map(lambda x: x.lstrip(left).rstrip(right))


def expandColumnFromString(dfcol, strpat):
    return dfcol.str.split(strpat, expand=True)


# use this date_parser function to convert date string to datetime values eg '%Y-%m-%d %I-%p'
pattern = '%Y-%m-%d %I-%p'


def d_parser(x):
    return pd.datetime.strptime(x, pattern)
