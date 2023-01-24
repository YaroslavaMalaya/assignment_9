import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data1 = pd.read_csv('titles.csv')
# data1.groupby('type')['imdb_score'].count().plot.pie()

names = ["movie", "show"]
values = [1,20]
plt.bar(names, values)
plt.show()

