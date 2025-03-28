#OPERaCIONES ENTRE CONJUNTOS
# | pipe
# & ampersant
# - diferencia
# ^ circunflejo
import random


a={1,2,3,4,5,7,9}
b={1,3,6,7,8,9,0}
print(a)
print(b)
union=a|b
print(f"union={union}")
inter=a&b
print(f"interseccion={inter}")
diferencia=a-b
print(f"diferencia={a-b}")
difsimetrica=a^b
print(f"difsimetrica={a^b}")

a=set()
b=set()
tam=random.randint(5,15)
for i in range(tam):
    num=random.randint(1,20)
    a.add(num)

tam=random.randint(5,15)
for i in range(tam):
    num=random.randint(1,20)
    b.add(num)

print(a)
print(b)
union=a|b
print(f"union={union}")
inter=a&b
print(f"interseccion={inter}")
diferencia=a-b
print(f"diferencia={a-b}")
difsimetrica=a^b
print(f"difsimetrica={a^b}")

print("subset1=",diferencia.issubset(a))
print("subset2=",diferencia.issubset(b))

print("superset1=",union.issuperset(a))
print("superset2=",union.issuperset(b))