personas = [{"nombre": "Mario", "edad": 49},
            {"nombre": "Ana", "edad": 32},
            {"nombre": "Luis", "edad": 41},
            {"nombre": "Marta", "edad": 28},
            {"nombre": "Javier", "edad": 55},
            ]


def media_edades(personas):
    suma_edades = 0
    media = 0
    for n in personas:
        suma_edades = suma_edades + n['edad']


    media = suma_edades / len(personas)
    return(media)


def persona_mayor_menor(personas):
    
    edad_mayor = -1
    nombre_edad_mayor = ""
    edad_menor = float('inf')
    nombre_edad_menor = ""
    
    for n in personas:
        if n['edad'] > edad_mayor:
            edad_mayor = n['edad']
            nombre_edad_mayor = n['nombre']

        if n['edad'] < edad_menor:
            edad_menor = n['edad']
            nombre_edad_menor = n['nombre']

    return(nombre_edad_mayor, edad_mayor, nombre_edad_menor, edad_menor)


def analiza_datos_personas(personas):
    media_edad = media_edades(personas)
    nombre_edad_mayor, edad_mayor, nombre_edad_menor, edad_menor = persona_mayor_menor(personas)

    datos_analizados = {"media_edad": media_edad, "nombre_edad_mayor": nombre_edad_mayor, "edad_mayor": edad_mayor, "nombre_edad_menor": nombre_edad_menor, "edad_menor": edad_menor}
    return datos_analizados

datos_analizados = analiza_datos_personas(personas)

print(f"La media de edad es: {datos_analizados['media_edad']}")
print(f"La persona mayor es: {datos_analizados['nombre_edad_mayor']} y tiene {datos_analizados['edad_mayor']} años")
print(f"La persona más joven es: {datos_analizados['nombre_edad_menor']} y tiene {datos_analizados['edad_menor']} años")


