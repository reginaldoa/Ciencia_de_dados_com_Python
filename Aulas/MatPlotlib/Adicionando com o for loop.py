import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

gas = pd.read_csv("bases_para_trabalhar/gas_prices.csv")
#print(gas)


list_country = ["Australia", "USA", "Canada"]


# Apesar do objetivo ser o mesmo, dessa forma, consigo fazer o código com algumas linhas a menos.
for country in gas:
    if country in list_country:
        plt.plot(gas["Year"], gas[country], label = [country], marker = ".")

plt.xticks(gas["Year"][::2])


plt.xlabel("Years") # Uma legenda na horizontal
plt.ylabel("US$")   # Uma legenda na vertical


plt.legend()
plt.show()