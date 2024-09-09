import pandas as pd

# Cleaning Data - fixing bad data in dataset like empty cells, data in wrong format, wrong data, duplicate data
df = pd.read_csv('data2.csv')

# Cleaning data of empty cells
df.dropna(inplace=True)             # remove rows with empty cell
                                    # if inplace argument is true which will overwrite existing dataframe into new dataframe

# new_dataframe = df.fillna(130)  # replace empty row with some user defined values

# Cleaning data of wrong format
# After removing wrong format of column and row
df.drop([26],inplace=True)      # remove rows with wrong format cell                
                                # Bydefault axis is 0 means row and 1 means column
df['Duration'] = pd.to_numeric(df['Duration'])
df['Date'] = pd.to_datetime(df['Date'])
df['Pulse'] = pd.to_numeric(df['Pulse'])
df['Maxpulse'] = pd.to_numeric(df['Maxpulse'])
df['Calories'] = pd.to_numeric(df['Calories'])

# Cleaning data of wrong input
# find wrong data and replace with another data
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120
# find wrong data and remove with another data
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x,inplace=True)

# Cleaning data with duplicated data
# print("Check for any duplicated data ->",df.duplicated())
df.drop_duplicates(inplace=True)    # remove rows with duplicate format cell
print(df)

# Mean, Median, Mode
# print("Mean of calories: ",df["Calories"].mean())
# print("Median of calories: ",df["Calories"].median())
# print("Mode of calories: ",df["Calories"].mode()[0])