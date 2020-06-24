
import pandas as pd

# replaces unwanted left and rightparts of a string


def replaceLeftRight(df, left, right):
    return df.map(lambda x: x.lstrip(left).rstrip(right))
