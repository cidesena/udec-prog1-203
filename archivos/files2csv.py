import csv

with open("archivos/customers.csv","r") as micsv:
    contenido=csv.reader(micsv)
    print(contenido)

    for linea in contenido:
        print(linea)
    
    
    datos=[["Index",91],["Customer Id","5ef6d3eefdD43b2"],["First Name","Nina"],["Last Name","Chavez"]]

    with open("archivos/customers.csv","a") as micsv:
        contenido=csv.writer(micsv)
        contenido.writerow(datos)