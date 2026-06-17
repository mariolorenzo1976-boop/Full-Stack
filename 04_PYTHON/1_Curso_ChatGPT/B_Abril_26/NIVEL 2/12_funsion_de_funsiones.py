personas = [{"nombre": "Mario", "edad": 49},
            {"nombre": "Ana", "edad": 32},
            {"nombre": "Luis", "edad": 41},
            {"nombre": "Marta", "edad": 28},
            {"nombre": "Javier", "edad": 55},
            ]


def media_edad(personas):

    media = 0
    contador = 0
    for n in personas:
        media = media + n['edad']
        contador += 1

    return(media/contador)

def max_min(personas):

    mayor_edad = -1
    menor_edad = float('inf')
    nombre_mayor = ""
    nombre_menor = ""
    for n in personas:
        if n['edad'] > mayor_edad:
            mayor_edad = n['edad']
            nombre_mayor = n['nombre']
        if n['edad'] < menor_edad:
            menor_edad = n ['edad']
            nombre_menor = n['nombre']

    return(nombre_mayor, mayor_edad , nombre_menor, menor_edad)


def analiza_personas(personas):
   
    dato_media = media_edad(personas)
    
    nombre_mayor, mayor_edad , nombre_menor, menor_edad = max_min(personas)

    return (dato_media, nombre_mayor, nombre_menor, mayor_edad, menor_edad)



dato_media, nombre_mayor, nombre_menor, mayor_edad, menor_edad = analiza_personas(personas)

print("la media es:", dato_media)
print(f"Mayor edad es de : {nombre_mayor} con {mayor_edad} años")
print(f"Menor edad es de : {nombre_menor} con {menor_edad} años")