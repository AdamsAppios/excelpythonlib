import pandas as pd
import numpy as np
import string
import random as rndm
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
current_directory = "\\".join(dir_path.split("\\")[0:-1])


def id_generator(chars=string.ascii_uppercase + string.digits):
    size = np.random.randint(low=3, high=10, size=None)
    return ''.join(rndm.choice(chars) for _ in range(size))


def np_tocolumns(columnlist):
    for i in range(0, len(columnlist)):
        if i == 0:
            newcol = columnlist[0]
        else:
            newcol = np.append(newcol, columnlist[i], axis=1)
    return newcol


df = pd.DataFrame(np.random.randint(
    0, 100, size=(100, 2)), columns=["Order#", "Cost"])
df2 = pd.DataFrame(np.random.randint(
    0, 100, size=(100, 4)), columns=list('ABCD'))
increment = np.arange(0, 100).reshape(100, 1)
randes = np.random.randint(0, 100, size=(100, 1))
customer_name = []
another_column = []
for i in range(0, 100):
    customer_name.append([id_generator()])
for i in range(0, 100):
    another_column.append([id_generator()])
customer_name = np.array(customer_name)
another_column = np.array(another_column)
newcol1 = np_tocolumns([increment, randes])
newcol2 = np_tocolumns([increment, randes, customer_name, another_column])
df1 = pd.DataFrame(data=newcol1, columns=["Order#", "Cost"])
df2 = pd.DataFrame(data=newcol2, columns=[
                   "Order#", "Cost", "CustomerName", "AnotherColumn"])
df1 = df1.iloc[::2]
df1.to_csv("{0}\\job22ss\\data1.csv".format(current_directory), index=False)
df2.to_csv("{0}\\job22ss\\data2.csv".format(current_directory), index=False)
