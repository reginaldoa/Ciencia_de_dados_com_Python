import numpy as np

a = np.array([[2,3,4,5] , [6,7,8,9]])
#print(a)



#Buscar o 8 , buscar a array[row,colu]
#Consigo filtrar dessa forma, independente de quantas listas estiverem na variável
print(a[1,2])


#Também dá pra fazer contagem regressiva
print(a[1,-2])

#Selecionando coluna
print(a[0, :])
print(a[1, :])


#Buscando apenas o 3 e o 7
print(a[0,1], a[1,1])
#OU
print(a[:,1]) # Dessa forma, volta como lista


produtos = np.array([["celular", "televisao"] ,[1000 , 2000]])

#Quero selecionar o valor da TV
print(produtos[:,1])