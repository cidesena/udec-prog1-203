with open("archivos/himno.txt","r",encoding="utf-8") as lector:
    contenido=lector.readlines()
    #print(type(contenido))
#print(contenido[5])

#print(contenido)
for linea in contenido:
    print(linea, end="")

