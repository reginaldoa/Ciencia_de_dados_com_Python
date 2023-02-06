#   Lendo os dados por ordem alfabética
import pandas as pd


dados = pd.read_csv('Bases_para_trabalhar/fifa.csv')

#print(dados)

# Filtrando nacionalidades
#print(dados.loc[dados['Nationality'] =='Argentina'])
#print(dados[dados['Nationality']== 'Spain'])

#Filtrando idade
#print(dados[dados['Age'] == 27])



#Filtrar de uma forma melhor
#print(dados.sort_values(['Name','Age'], ascending= False))

#Verificando jogador mais pesado
#print(dados.sort_values("Weight"))

#Filtrando nome e peso dos jogadores
print(dados[['Name','Weight']])