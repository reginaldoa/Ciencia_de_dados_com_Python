import pandas as pd


dados = pd.read_csv("Bases_para_trabalhar/fifa.csv")

dados['total'] = dados['Acceleration'] + dados ['Agility'] + dados ['Reactions']
#dados['teste'] = 'teste'

#print(dados[['Name','total']]) Aqui está puxando pelo número do índice
print(dados.sort_values('total', ascending= False)) #A idéia aqui é fazer uma classificação do maior para menor, por isso o ascending em False
