import pandas as pd

# Data Correlations - finding the relationship between columns in data set

'''

Rules of Correlation: -
--------------------
    1. The number varies from -1 to 1.
    2. If number is 1 then perfect correlation.
    3. If number is 0.9, 0.6 then good correlation.
    4. If number is -0.9, -0.6 then average correlation i.e., if one value increases then other value will decreases.
    5. If number is 0.2 then bad correlation.

'''

df = pd.read_csv('data3.csv')

df['Duration'] = pd.to_numeric(df['Duration'])
df['Pulse'] = pd.to_numeric(df['Pulse'])
df['Maxpulse'] = pd.to_numeric(df['Maxpulse'])
df['Calories'] = pd.to_numeric(df['Calories'])

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print(df.corr())