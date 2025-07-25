import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [5, 15, 25, 35, 45, 55]}

df = pd.DataFrame(data)
print(df)

def custom_agg(x):
    return x.max() - x.min()

df1 = df.groupby('Category').agg(custom_agg)
print(df1)