import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(
    0, 100, size=(100, 4)), columns=list('ABCD'))
df.to_csv("job1/data1.csv")
df2 = pd.DataFrame(np.random.randint(
    0, 100, size=(100, 4)), columns=list('ABCD'))
df2.to_csv("job1/data2.csv")
