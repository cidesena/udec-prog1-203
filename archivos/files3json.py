import json

with open("archivos/people.json","r") as eljson:
    contenido=json.load(eljson)
    print(type(contenido))

for p in contenido:
    print(p["name"])
    print("-"*25)

datos={
    "name": "Jaime Diaz",
    "language": "spanish",
    "id": "ENTOCR13RSCLZ6KB",
    "bio": "Eget malesuada nibh efficitur et. Pellentesque massa sem, scelerisque sit amet odio id, cursus tempor urna. Etiam congue dignissim volutpat. Vestibulum pharetra libero et velit gravida euismod.",
    "version": 1.9
  }

with open("archivos/people.json","a") as eljson:
    json.dump(datos,eljson,indent=4)

