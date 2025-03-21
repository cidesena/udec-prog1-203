import random
Uname="Universidad de Cundinamarca"
otra=[10,20,30]
listaU=[letra for letra in Uname]
print(listaU)
listaU=[x for x in otra]
print(listaU)
lista=[random.randint(1,100) for i in range(random.randint(5,15))]
print(lista)
#pares=[x if x%2==0 else "" for x in lista]
pares=[x for x in lista if x%2==0]
print(pares)
print(lista.sort())

