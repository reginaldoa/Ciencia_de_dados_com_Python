import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

gas = pd.read_csv("bases_para_trabalhar/gas_prices.csv")
#print(gas)


plt.plot(gas["Year"], gas["Australia"], 'r.-' , label = "Australia")
plt.plot(gas["Year"], gas["Italy"], 'y.-' , label = "Italia")
plt.plot(gas["Year"], gas ["USA"], 'b.-', label = "Estados Unidos")
plt.plot(gas["Year"], gas["Japan"], 'g.-' ,label =" Japão")

plt.xticks(gas["Year"][::2])


plt.xlabel("Years") # Uma legenda na horizontal
plt.ylabel("US$")   # Uma legenda na vertical


plt.legend()
plt.show()