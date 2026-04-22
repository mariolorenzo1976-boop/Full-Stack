personas = [{'nombre': 'Mario', 'edad': 49},
            {'nombre': 'Ana', 'edad': 32},
            {'nombre': 'Luis', 'edad': 41},
            {'nombre': 'Marta', 'edad': 28},
            {'nombre': 'Javier', 'edad': 55},
            {'nombre': 'Lucia', 'edad': 40},
            {'nombre': 'Pedro', 'edad': 36},
            {'nombre': 'Sofía', 'edad': 44},
            ]


mayor_40 =[n['nombre'] for n in personas if n['edad']>40]
menor_igual_40 =[n['nombre'] for n in personas if n['edad']<=40]

cantidad_mayor_40 = len(mayor_40)
cantidad_menor_igual_40 = len(menor_igual_40)

print(f"Mayores de 40: {mayor_40}")
print(f"Menores o iguales de 40: {menor_igual_40}")

print(f"Cantidad mayores: {cantidad_mayor_40}")
print(f"Cantidad menores o igual: {cantidad_menor_igual_40}")


