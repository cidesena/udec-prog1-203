# lista=[]
# print(type(lista))
# #lista.append(100)#lista[0]=100
# cantidad=int(input("que cantidad de numeros?"))
# for i in range(cantidad):
#     num=int(input("ingrese numero"))
#     lista.append(num)

# print(lista)

import random
cantidad=random.randint(5,15)
vector=[]
for i in range(cantidad):
    num=random.randint(1,100)
    vector.append(num)

print(vector)
print(f"tamaño={len(vector)}")

for i in range(len(vector)):
    if i%2==0:
        print(vector[i],end=" ")
print()
for i in range(0,len(vector),2):
     print(vector[i],end=" ")
print()
for i in range(len(vector)):
    if i%2!=0:
        print(vector[i],end=" ")
print()
for i in range(1,len(vector),2):
     print(vector[i],end=" ")