import pandas as pd 

df = pd.read_csv("Bases_para_trabalhar/house.csv")

#print(df.head(5))


filter1 = df.loc[(df['Rooms'] == 3) & (df["Type"] == 'h') & (df['Price'] <= 500000)]

print(filter1)