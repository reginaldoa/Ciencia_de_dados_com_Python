import pandas as pd 

df = pd.read_csv("Bases_para_trabalhar/house.csv")

#print(df.groupby(["SellerG"]).mean()) # média
#print(df.groupby(['SellerG']).sum().sort_values('Price', ascending= False).head(10)) #calcular os 10 que vendem 
#mais, de cima pra baixo


#print(df.groupby(["SellerG"]).sum().sort_values("Rooms", ascending= False).head(10)) #calcular os 10 que vendem 
#mais quartos, de cima pra baixo

print(df.groupby(["SellerG"]).count()) #contando 