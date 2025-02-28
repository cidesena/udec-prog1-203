
x=True
print(type(x))

if True:
    print("Esto ocurre una sola vez")
cont=0
while True:
    print("Este ciclo es infinito")
    cont+=1
    if cont==5:
        break

num=1
cont=0
while num!=0:
    num=int(input("ingrese numero"))
    cont+=1
else:
    print(f"Usted ingreso {cont} numeros")

