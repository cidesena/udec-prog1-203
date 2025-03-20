import random

def llenarLista(cantidad):
    lista=[]
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

def sumaLista(lista):
    suma=0
    for num in lista:
        suma+=num
    return suma

def sumaParLista(lista):
    suma=0
    for num in lista:
        if num%2==0:
            suma+=num
    return suma

def sumaImparLista(lista):
    suma=0
    for num in lista:
        if num%2!=0:
            suma+=num
    return suma

vec1=llenarLista(random.randint(5,10))
vec2=llenarLista(random.randint(5,10))
vec3=llenarLista(random.randint(5,10))

print(vec1)
print(sumaLista(vec1))
print(sumaParLista(vec1))
print(sumaImparLista(vec1))
print(vec2)
print(sumaLista(vec2))
print(sumaParLista(vec2))
print(sumaImparLista(vec2))
print(vec3)
print(sumaLista(vec3))
print(sumaParLista(vec3))
print(sumaImparLista(vec3))

