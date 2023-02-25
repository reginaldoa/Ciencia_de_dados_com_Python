import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

gas = pd.read_csv("bases_para_trabalhar/gas_prices.csv")

print(gas)

#Comparar preço do gás entre 3 países

plt.plot(gas['Year'] , gas['Australia']) 
plt.plot(gas['Year'] , gas['Italy'])
plt.plot(gas['Year'] , gas['USA'])

print(plt.show())