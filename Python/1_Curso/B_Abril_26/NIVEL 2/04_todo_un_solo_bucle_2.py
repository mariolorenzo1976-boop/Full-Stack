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

nombre_mayor= ""
edad_mayor = -1

nombre_menor = ""
edad_menor = float('inf')
edad_par = 0
i = 0

for n in personas:
    if n['edad'] > 40:
        nombres_mayor_40.append(n['nombre'])
        i = i + 1
    else:
        nombres_menores_40.append(n['nombre'])
    
    if n['edad']>edad_mayor:
        edad_mayor = n['edad']
        nombre_mayor = n['nombre']
        

    if n['edad'] <= edad_menor:
        nombre_menor = n['nombre']
        edad_menor = n['edad']

    if n['edad'] % 2 == 0:
        edad_par +=1


    suma_edades = suma_edades + n['edad']



print("Media de edad:", suma_edades / len(personas))

print("Persona más mayor:", nombre_mayor, edad_mayor)
print("Persona más joven:", nombre_menor, edad_menor)

print("Mayores de 40:", nombres_mayor_40)
print("Menores o iguales de 40:", nombres_menores_40)

print("Personas con edad par", edad_par)

print(i)