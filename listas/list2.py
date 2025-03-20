import random
cantidad=random.randint(5,15)
vector=[]
for i in range(cantidad):
    num=random.randint(1,100)
    vector.append(num)
print(vector)

pares=[]
impares=[]
for i in range(len(vector)):
    if vector[i]%2==0:
        pares.append(vector[i])
    else:
        impares.append(vector[i])
print(pares)
print(impares)

spar=0
for x in vector:
    if x%2==0:
        spar+=x
print(f"suma de pares={spar}")
