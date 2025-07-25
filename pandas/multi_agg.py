import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [10, 20, 30, 40, 50, 60]}

df = pd.DataFrame(data)
print(df)
df1=df.groupby('Category').agg(['sum','mean','max'])
print(df1)