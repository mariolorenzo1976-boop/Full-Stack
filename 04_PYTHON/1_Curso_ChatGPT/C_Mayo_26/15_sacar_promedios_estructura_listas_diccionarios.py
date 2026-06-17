# Ejercicio 15 - promedios en estructuras de listas y diccionarios (primero agrupo, luego calculo y finalmente imprimo)
datos = [
    ("ana", 10),
    ("juan", 20),
    ("ana", 30),
    ("juan", 5),
    ("ana", 15),
    ("maria", 50)
]

promedio = {}

for clave, valor in datos:
    if clave not in promedio:
        promedio[clave] = []
    
    promedio[clave].append(valor) 

resultado = {}

for clave, valor in promedio.items():
    resultado[clave] = sum(valor) / len(valor)



print(resultado)


