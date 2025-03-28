# x={1,2,3,4,5,1,6}
# print(type(x))
# print(x)
# lista=[10,20,30]
# y=set(lista)
# print(type(x))
# print(y)
# lista.append(100)

import random


c1=set()
c1.add(10)
print(c1)
c1.add(11)
print(c1)
lista=[9,8,7]
tupla=(23,24,9,7,8)
c2={55,56}
c1.update(c2)
print(c1)
c1.update(lista)
print(c1)
c1.update(tupla)
print(c1)
#No indexable
#for i in range(len(c2)):
#print(c2[0])
for elemento in c1:
    print(elemento)
print(155 in c2)

#v={}
# print(type(v))
original=set()
duplicados=set()
tam=random.randint(5,15)
for i in range(tam):
    num=random.randint(1,20)
    if num not in original:
        original.add(num)
    else:
        duplicados.add(num)
print(original)
print(duplicados)

c3={1,2,3,4,5,6,7,8,9}
c3.discard(4)
print(c3)
print(c3.pop())
print(c3)
c3.clear()
print(c3)