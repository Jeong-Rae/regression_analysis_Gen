
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

size=100

data_x=[i for i in range(size)]
data_y=[ round((2+random.uniform(-1,1))*i + random.randint(-10,10),2) for i in data_x]
a, b = [0,100], [0,200]
plt.scatter(data_x, data_y)
plt.plot(a,b)
plt.show()

df, df['y'] = pd.DataFrame(data_x, columns = ['x']), data_y
df.to_csv("randomdataset.csv", index = False)
print(df)