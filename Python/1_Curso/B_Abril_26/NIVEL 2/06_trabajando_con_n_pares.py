personas = [{'nombre': 'Mario', 'edad': 49},
            {'nombre': 'Ana', 'edad': 32},
            {'nombre': 'Luis', 'edad': 41},
            {'nombre': 'Marta', 'edad': 28},
            {'nombre': 'Javier', 'edad': 55},
            {'nombre': 'Lucia', 'edad': 40},
            {'nombre': 'Pedro', 'edad': 36},
            {'nombre': 'Sofía', 'edad': 44},
            ]

nombres_pares = []
contador_pares = 0
suma_par = 0

for n in personas:
    if n['edad'] %2 == 0:
        nombres_pares.append(n['nombre'])
        contador_pares +=1
        suma_par = suma_par + n['edad']

print("Personas con edad par:", nombres_pares)
print("Cantidad de pares:", contador_pares)
print("Media de edades pares:", suma_par / contador_pares)
