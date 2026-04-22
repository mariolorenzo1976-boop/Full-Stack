personas = [{"nombre": "Mario", "edad": 49},
            {"nombre": "Ana", "edad": 32},
            {"nombre": "Luis", "edad": 41},
            {"nombre": "Marta", "edad": 28}
            ]

contador = 0
suma_edad = 0
cont_mayor_edad = 0
mayor_edad = []
for n in personas:
    if n['edad']>40:
        suma_edad = suma_edad + n['edad']
        contador = contador + 1
    
    if n['edad'] > cont_mayor_edad:
        cont_mayor_edad = n['edad']
        mayor_edad = [n['nombre'], n['edad']]


if contador > 0:
    print(suma_edad / contador)
    print(f"Hay {contador} personas con más de 40 años")
else:
    print("No hay personas mayores de 40 años")

print(f"La persona mayor es {mayor_edad}")

