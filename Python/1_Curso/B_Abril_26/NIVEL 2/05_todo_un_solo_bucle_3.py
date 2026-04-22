personas = [{'nombre': 'Mario', 'edad': 49},
            {'nombre': 'Ana', 'edad': 32},
            {'nombre': 'Luis', 'edad': 41},
            {'nombre': 'Marta', 'edad': 28},
            {'nombre': 'Javier', 'edad': 55},
            {'nombre': 'Lucia', 'edad': 40},
            {'nombre': 'Pedro', 'edad': 36},
            {'nombre': 'Sofía', 'edad': 44},
            ]


mayor_40 = -1 
menor_40 = float('inf')

nombre_mas_mayor = ""
nombre_mas_joven = ""

contador_mayor = 0
contador_menor = 0

edad_mayor = 0
edad_joven = 0

suma_edades = 0

numero_pares = 0

veces_entro = 0


for n in personas:

    if n['edad'] > mayor_40:
        mayor_40 = n['edad']
        nombre_mas_mayor = n['nombre']
        edad_mayor = n['edad']
       
   
    if n['edad'] <= menor_40:
        menor_40 = n['edad']
        nombre_mas_joven = n['nombre']
        edad_joven = n['edad']
        

    if n['edad'] > 40:
        contador_mayor +=1
    else:
        contador_menor +=1
       
    
    if n['edad'] %2 == 0:
        numero_pares +=1
    
    suma_edades += n['edad']
   
    
print("Media de edad:", (suma_edades / len(personas)))

print(f"Person más mayor: {nombre_mas_mayor} , {edad_mayor}")
print(f"Person más joven: {nombre_mas_joven} , {edad_joven}")

print("Mayores de 40:", contador_mayor)
print("Menores o igual de 40:", contador_menor)

print("Pares:", numero_pares)


