personas = [{'nombre': 'Mario', 'edad': 49},
            {'nombre': 'Ana', 'edad': 32},
            {'nombre': 'Luis', 'edad': 41},
            {'nombre': 'Marta', 'edad': 28},
            {'nombre': 'Javier', 'edad': 55},
            {'nombre': 'Lucia', 'edad': 40},
            {'nombre': 'Pedro', 'edad': 36},
            {'nombre': 'Sofía', 'edad': 44},
            ]

nombres_mayor_40 = []
nombres_menores_40 = []
suma_edades = 0

nombre_mayor= 0
edad_mayor = 0

nombre_menor = 0
edad_menor = 40

for n in personas:
    if n['edad'] > 40:
        nombres_mayor_40.append(n['nombre'])
        if n['edad'] > edad_mayor:
            nombre_mayor = n['nombre']
            edad_mayor = n['edad']

    else:
        nombres_menores_40.append(n['nombre'])
        if n['edad'] <= edad_menor:
            nombre_menor = n['nombre']
            edad_menor = n['edad']
    
    suma_edades = suma_edades + n['edad']



print("Media de edad:", suma_edades / len(personas))

print("Persona más mayor:", nombre_mayor, edad_mayor)
print("Persona más joven:", nombre_menor, edad_menor)

print("Mayores de 40:", nombres_mayor_40)
print("Menores o iguales de 40:", nombres_menores_40)
