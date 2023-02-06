import pandas as pd



dados = pd.read_csv('Bases_para_trabalhar/fifa.csv') #caminhoPasta/nomeArquivo
#exemplo ... dados_xlsx = pd.read_excel('Bases_para_trabalhar/fifa.xlsx')
#exemplo ... dados_txt = pd.read_csv('Bases_para_trabalhar/fifa.txt', delimiter='\t')

#print(dados) # Mostrar a tabela

#Mostra as primeiras entradas
#print(dados.head(2)) 

print()
print()
print()
print()

#Mostra as últimas entradas
#print(dados.tail(8)) 


#Visualizar quais são as colunas
#print(dados.columns) 


#Visualizar quais são as linhas
#print(dados.index)


#Filtrando as colunas
#print(dados[['Name','Nationality','Wage']])

#Filtrando dado de jogador(es) especifico
print(dados.iloc[1,2]) #primeiro é a linha, depois da vírgula é a coluna