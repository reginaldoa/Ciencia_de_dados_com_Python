#Exportar dados para algum arquivo

import pandas as pd


dados = pd.read_csv("Bases_para_trabalhar/fifa.csv")

dados['total'] = dados['Acceleration'] + dados ['Agility'] + dados ['Reactions'] # Critérios para definir os melhores.

print(dados[['Name', 'total']])


dados = dados[['Name', 'total']] # salvando apenas o que quero filtrar, na hora de importar 

#print(dados.sort_values("total", ascending= False))


dados.to_csv('dados1.csv', index= False)
dados.to_excel('dados2.xlsx', index= False)
dados.to_csv('dados3.txt', index= False, sep = '\t')