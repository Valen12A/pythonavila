#pares raiz
#impares potencia
import random 
import math 
tam = random.randint(5, 10)

lista =[random.randrange (100) for i in range (tam)]
lista2 = [i for i in lista]
print (lista)

par =[x for x in lista if x%2 == 0]
print (par)


 