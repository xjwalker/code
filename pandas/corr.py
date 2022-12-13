import pandas as pd

df = pd.DataFrame()

df = pd.read_csv('data.csv')


print(df.corr())