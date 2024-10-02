Pandas (Known as Pannel Data)

import pandas as pd

# Series -> It is one dimensional array holding data of any type.
a = [1,3,5,7]
print(pd.Series(a))

# user-defined index, data type, name
print(pd.Series(a,index=['first-index','second-index','third-index','fourth-index'], dtype='float64', name='Example of Series'))

# Data Frame -> It is two dimensional array holding data of any type.
print(pd.DataFrame(a))

# user-defined index, data type, name
print(pd.Series(a,index=['a','b','c','d'],dtype='float64',name='Example of Data Frame'))

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[[0,1,2]])   # locate row returns one or more specified rows

# CSV file
df = pd.read_csv('data1.csv')
print(df)
print('Number or rows in data.csv file ->',df.shape[0])
print('Number of columns in data.csv file ->',df.shape[1])

# JSON file
df = pd.read_json('data1.json')
print(df)
print('Number or rows in data.json file ->',df.shape[0])
print('Number of columns in data.json file ->',df.shape[1])

# Viewing data
df = pd.read_csv('data1.csv')
print("Head Bydefault: -",df.head(),sep='\n')    # head bydefault retrive data of top 5 rows
print("Head N nos.: -",df.head(10),sep='\n')     # head N nos., where N is user input
print("Tail Bydefault: -",df.tail(),sep='\n')    # head bydefault retrive data of bottom 5 rows
print("Tail N nos.: -",df.tail(10),sep='\n')     # head N nos., where N is user input
print("Information about dataset: -")
data_info = df.info()                            # describle dataset
