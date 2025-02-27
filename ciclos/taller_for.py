rango=range(0,10,2)
print(rango)
for i in range(10):
    print(i)

for i in range(1,15):
    print(i)

for i in range(50):
    print(f"carambola number {i}")

n=int(input("ingrese numero"))
for i in range(1,n):
    print(f"valor {i} respuesta={i*i}")
    #print("valor", i*i, "respuesta=", i*i)

for i in range(99,0,-3):
    #print(i)
    print(i,end=" ")

inicio=int(input("donde inicia"))
tope=int(input("donde termina"))
step=int(input("de cuanto en cuanto"))

for i in range(inicio,tope,step):
    print(i)