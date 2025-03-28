import random
lista=[100]
x=90
escalar=(100)
tupla=(100,)
print(type(lista))
print(type(tupla))
lista.append(12)
#tupla.append(100)
t=(1,2)
print(type(t))
print(t)
t=t+(10,)
print(t)

def crearTupla():
    tupla=()
    cantidad=random.randint(5,15)
    for i in range(cantidad):
        tupla+=(random.randint(1,100),)
    return tupla
tupla1=crearTupla()
print(tupla1)
print(tupla1[0])
print(tupla1[-1])

def sumaTupla(tt):
    suma=0
    for x in tt:
        suma+=x
    return suma

def meanTupla(ttt):
    return sumaTupla(ttt)/len(ttt)

tup=(1,2,3)
print(sumaTupla(tupla1))
print(sumaTupla(tup))

print(meanTupla(tupla1))
print(meanTupla(tup))
