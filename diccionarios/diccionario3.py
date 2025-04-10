#indexación y slicing
import random
lista=[10,30,20,50,5,7,11,21,31,100]
print(lista[0])
print(lista[5])
print(lista[-1])
print(lista[1:4])
print(lista[0:5])
print(lista[:5])
print(lista[-1:-6:-1])
print(lista[::2])
print(lista[-2::-2])
print(lista[-6:-1])
print(lista[5:11])
print(lista[5:])

tam=1
while tam%2!=0:
    tam=random.randint(10,20)
    print(tam)

lista=[random.randint(1,100) for i in range(tam)]


# sum1=0
# sum2=0
# mitad=len(lista)//2
# print(f"mitad={mitad}")
# for x in lista[:mitad]:
#     sum1+=x
# for x in lista[mitad:]:
#     sum2+=x

# print(f"suma primera mitad es:{sum1}")
# print(f"suma segunda mitad es:{sum2}")
# print(f"media primera mitad es:{sum1/mitad}")
# print(f"media segunda mitad es:{sum2/mitad}")

# sum3,sum4=(0,0)
# for x in lista[::2]:
#     sum3+=x
# for x in lista[1::2]:
#     sum4+=x

# print(f"suma 3={sum3}")
# print(f"suma 4={sum4}")
# print(f"media 3={sum3/mitad}")
# print(f"media 4={sum4/mitad}")
print("-"*50)
tupla=()
for num in range(tam):
    tupla+=(random.randint(1,100),)
print(f"tupla:{tupla}")

sum1=0
sum2=0
mitad=len(tupla)//2
print(f"mitad={mitad}")
for x in tupla[:mitad]:
    sum1+=x
for x in tupla[mitad:]:
    sum2+=x

print(f"suma primera mitad es:{sum1}")
print(f"suma segunda mitad es:{sum2}")
print(f"media primera mitad es:{sum1/mitad}")
print(f"media segunda mitad es:{sum2/mitad}")

sum3,sum4=(0,0)
for x in tupla[::2]:
    sum3+=x
for x in tupla[1::2]:
    sum4+=x

print(f"suma 3={sum3}")
print(f"suma 4={sum4}")
print(f"media 3={sum3/mitad}")
print(f"media 4={sum4/mitad}")