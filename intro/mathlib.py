
import math
print(math.pow(10,2))
print(math.sqrt(100))
a,b,c=0,0,0
a=int(input("ingrese a"))
b=int(input("ingrese b"))
c=int(input("ingrese c"))
raiz=(b**2)-(4*a*c)
print(raiz)
if raiz<0:
    print("indeterminacion")
elif a==0:
    print("indeterminacion")
else:
    r1=((b*-1)+math.sqrt(raiz))/(2*a)
    r2=((b*-1)-math.sqrt(raiz))/(2*a)
    print(f"raiz 1= {r1}")
    print(f"raiz 2= {r2}")
