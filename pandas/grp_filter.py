import pandas as pd
# Sample DataFrame
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)
print(df)
df2 = df.groupby('Category').sum()
print(df2)
##df1= df.groupby('Category').filter(lambda x: x['Value'].sum()>5)
##print(df1)