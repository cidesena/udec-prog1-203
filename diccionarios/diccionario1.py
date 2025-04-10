persona={"nombre":"Angela Martinez",
         "nombre1":"Angela Martinez",
          "documento":1234566,
          "correo":"amartinez@mail.com",
         "clases":["programacion","algebra","estadistica"],
        "ubicacion":{
            "municipio":"Soacha",
            "barrio":"San Mateo"
        } 
}
print(type(persona))
print(persona)
print(persona['ubicacion'])
print(persona['documento'])
persona["promedio"]=3.5
print(persona)
#persona.clear()
x=persona.copy()
print(x)
# claves=("universidad","programa")
# valores=None
# academia=dict.fromkeys(claves,valores)
# print(academia)
print(persona.keys())
print(persona.values())
print(persona.items())
for key in persona.keys():
    print(key)
for val in persona.values():
    print(val)
for key,value in persona.items():
    print(f"Clave:{key}")
    print(f"Valor:{value}")

print("document" in persona.keys())



