import pandas as pd
# Sample DataFrame
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Type': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
        'Value': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)
print(df)
df1 = df.groupby(['Category','Type']).sum('value')
print(df1)
df2 = df.groupby(['Category']).sum('value')
print(df2)