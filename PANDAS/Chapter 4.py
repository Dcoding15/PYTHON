import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data3.csv')

df.plot()

plt.show()


# Pivot table
# pd.pivot(index="",columns="",values=[])

# Melting data frame
# pd.melt(df, id_vars=[""], value_vars=[""])
