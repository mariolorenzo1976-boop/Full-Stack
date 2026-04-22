personas = [{'nombre': 'Mario', 'edad': 49},
            {'nombre': 'Ana', 'edad': 32},
            {'nombre': 'Luis', 'edad': 41},
            {'nombre': 'Marta', 'edad': 28},
            {'nombre': 'Javier', 'edad': 55},
            {'nombre': 'Lucia', 'edad': 40},
            {'nombre': 'Pedro', 'edad': 36},
            {'nombre': 'Sofía', 'edad': 44},
            ]

mayor_40 = []
menor_igual_40 = []
contador_mayor_40 = 0
contador_menor_40 = 0

for n in personas:
    if n['edad'] > 40:
        mayor_40.append(n['nombre'])
        contador_mayor_40 +=1
    else:
        menor_igual_40.append(n['nombre'])
        contador_menor_40 +=1

print("Mayores de 40:", mayor_40)
print("Menores o igual de 40:", menor_igual_40)

print("Cantidad mayores:", contador_mayor_40)
print("Cantidad menores o iguales:", contador_menor_40)



