# def saludar(nombre):
#     return f"Hola {nombre}"

# print(saludar("Tito"))
# x=saludar("Tito")
# print(saludar("Tato"))
# print(saludar("Teto"))
# print(saludar("Tata"))

def perfecto(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return f"{num} es perfecto"
    else:
        return f"{num} no es perfecto"

def divisores(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            print(f"{i} es divisor de {num}")
    
divisores(10)
divisores(6)



print(perfecto(10))
print(perfecto(6))
print(perfecto(20))
print(perfecto(28))