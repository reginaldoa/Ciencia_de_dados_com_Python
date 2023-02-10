import pandas as pd
import re 

df = pd.read_csv("Bases_para_trabalhar/house.csv")

#print(df.head(5))



#teste = df.loc[df["Suburb"] == "Abbotsford"]
#print(teste)


filter2 = df.loc[df["Address"].str.contains('Turner St| Turner Rd', flags=re.I )] #Tirando o case sensitive.
print(filter2)
