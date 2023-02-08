import pandas as pd

df = pd.read_csv('Bases_para_trabalhar/house.csv')

print(df.head(10))

print(df[df["Address"]== '49 Lithgow St'])

print(df["Address"])