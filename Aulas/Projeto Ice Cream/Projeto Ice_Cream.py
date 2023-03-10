import pandas as pd
import matplotlib.pyplot as plt

#Objetivo

# Criar gráfico de forma bem visual, que quando a temperatura sobe as vendas aumentam (sorvetes) 
#Quando a temperatura diminui, as vendas diminui junto (sorteve)

# Professor mostrou um gráfico como exemplo

sorveteria = pd.read_csv("Bases_para_trabalhar/sorveteria.csv")
print(sorveteria)


plt.title("Ice Cream Truck")

plt.plot(sorveteria["Temperature"], sorveteria["Sales"], 'r.--',  label = "US$")



plt.xlabel("Temperature") #Uma legenda na vertical
plt.ylabel("Sales") #Uma legenda na horizontal



plt.legend()
plt.show()

#Exercício resolvido, como solicitado no desafio.