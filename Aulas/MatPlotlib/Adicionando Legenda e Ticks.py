import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


gas = pd.read_csv("Bases_para_trabalhar/gas_prices.csv")
plt.title("Valores do combustível em  US$")

#O  eixo X é o horizontal
#O  eixo Y é o vertical

#print(gas)
plt.plot(gas['Year'], gas['Australia'], label = "Austrália")
plt.plot(gas['Year'], gas['Italy'], label = "Itália")
plt.plot(gas['Year'], gas['USA'], label = "Estados Unidos")
plt.plot(gas['Year'], gas['Japan'], label = "Japão")

plt.xticks(gas['Year'] [: : 2]) #Mostrando o ano no formato correto de 2 em 2 anos

print(plt.legend())
print(plt.show())
