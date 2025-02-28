inicio=int(input("donde inicia"))
tope=int(input("donde termina"))
step=int(input("de cuanto en cuanto"))

for i in range(inicio,tope,step):
    if i%7==0:
        print(f"{i} es multiplo de 7")
    else:
        print(i)
    
num=int(input("ingrese numero"))
cont=0
for i in range(1,num+1):
    if num%i==0:
        cont+=1
        #print(f"{i} Es divisor")
if cont==2:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")
    
