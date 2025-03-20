def sumaDigitos(num):
    suma=0
    digito=0
    while num>0:
        #digito=num%10        
        #suma+=digito
        suma+=digito%10
        num//=10
        print(f"num={num}")
    return suma

print(sumaDigitos(123))    
