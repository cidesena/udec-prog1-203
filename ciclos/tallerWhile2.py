import random
num=random.randint(1,20)
print(num)
num2=1
cont=0
while num!=num2:
    num2=int(input("ingrese numero"))
    cont+=1

print(f"numero de intentos={cont}")

