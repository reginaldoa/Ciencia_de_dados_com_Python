#Mudando o nome do vendedor em todos os campos

import pandas as pd

df = pd.read_csv("Bases_para_Trabalhar/house.csv")

#print(df)

df.loc[df["SellerG"] == "Nelson" , "SellerG"] = "Reginaldo"
#       nessa coluna    esse nome  nessa coluna  vira esse nome

df.loc[df["SellerG"] == "Reginaldo", ["Method"]] = "Pending"

#print(df.loc[df["SellerG"] == "Reginaldo"])

df = df[["SellerG","Method"]]

#print(df)

print(df.loc[df["SellerG"] == "Reginaldo"])