personas = {"nombre": "Mario", "edad": 49, "ciudad": "Tenerife" }

for clave in personas:
    print(clave)

for valor in personas.values():
    print(valor)


for clave, valor in personas.items():
    print(clave,valor)
    