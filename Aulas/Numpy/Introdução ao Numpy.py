#Consegue manipular grandes quantidades de listas (listas)
import numpy as np
import sys 


a = [1,2,3,4,5]
b = np.array([1,2,3,4,5]) # Gasta menos espaço


print(a)
print("**********************")
print(b)

print(sys.getsizeof(a))
print(b.nbytes)