import pandas as pd
import re 

df = pd.read_csv("Bases_para_trabalhar/house.csv")

#Mudar pra uma casa que o número seja 59 e seja abaixo de 500 mil dolares

filter3 = df.loc[df['Address'].str.contains('^59', flags= re.I) & (df['Price'] <= 500000)]
print(filter3)