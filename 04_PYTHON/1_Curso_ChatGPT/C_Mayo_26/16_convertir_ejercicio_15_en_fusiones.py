# Ejercicio 16 - el ejercicio 15 en fusiones

def agrupar(datos):

    promedio = {}

    for clave, valor in datos:
        if clave not in promedio:
            promedio[clave] = []
    
        promedio[clave].append(valor) 

    return promedio

def resultado(promedio):

    resultado = {}

    for clave, valor in promedio.items():
        resultado[clave] = sum(valor) / len(valor)

    return resultado


datos = [
    ("ana", 10),
    ("juan", 20),
    ("ana", 30),
    ("juan", 5),
    ("ana", 15),
    ("maria", 50)
]


agrupados = agrupar(datos)
promedios = resultado(agrupados)

print(f"La fusión agrupados da como resltado: , {agrupados}  y la fusión promedios da como resultado: , {promedios}")