personas = [{"nombre": "Mario", "edad": 49},
            {"nombre": "Ana", "edad": 32},
            {"nombre": "Luis", "edad": 41},
            {"nombre": "Marta", "edad": 28},
            {"nombre": "Javier", "edad": 55},
            ]



def analiza_personas(personas):
    mayor_edad = -1
    menor_edad = float('inf')
    nombre_mayor_edad = ""
    nombre_menor_edad = ""
    contador = 0
    suma_edades = 0
    for n in personas:
        if n['edad'] > mayor_edad:
            mayor_edad = n['edad']
            nombre_mayor_edad = n['nombre']

        if n['edad'] < menor_edad:
            menor_edad = n['edad']
            nombre_menor_edad = n['nombre']
        contador += 1
        suma_edades = suma_edades + n['edad']

    media = suma_edades / contador 

    resultado = {"media": media, "nombre_mayor": nombre_mayor_edad, "edad_mayor": mayor_edad, "nombre_menor": nombre_menor_edad, "edad_menor":menor_edad}
    return(resultado)


resultados = analiza_personas(personas)
print(f"La media de edades es:{resultados['media']}")
print(f"{resultados['nombre_mayor']} con edad: {resultados['edad_mayor']} es el/la mayor")
print(f"{resultados['nombre_menor']} con edad: {resultados['edad_menor']} es el/la más joven")


