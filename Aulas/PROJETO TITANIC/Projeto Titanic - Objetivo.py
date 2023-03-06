# 1° parte - O objetivo é aparecer a contagem de ID, trazer na ordem = nome, idade, sexo, classe, sobreviventes
#   Fazer os seguintes filtros
# 2° parte -Fazer um filtro somente para mulheres
# 3° parte - Fazer um filtro da primeira classe
# 4° parte -Fazer um filtro de sobreviventes
# 5° parte - Colocar os nomes na ordem alfabética.

import pandas as pd 
titanic = pd.read_csv("Bases_para_trabalhar/titanic.csv")

titanic = titanic[["Name", "Age", "Sex", "Pclass", "Survived"]] # 1° parte
titanic = titanic.loc[titanic["Sex"].str.contains("female")] # 2° parte
titanic = titanic.loc[titanic["Pclass"] == 1] # 3° parte
titanic = titanic.loc[titanic["Survived"] == 1] #4° parte 
titanic = titanic.sort_values(by = "Name") # 4° parte

print(titanic)

#Exercício finalizado.
