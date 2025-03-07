def divisores(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            print(f"{i} es divisor")
    
divisores(10)
divisores(6)