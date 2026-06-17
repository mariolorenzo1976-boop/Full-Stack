# 1 Conteo
datos = ["rojo", "azul", "rojo", "verde", "azul", "rojo"]

conteo = {}

for n in datos:
    if n not in conteo:
        conteo[n] = 0
    conteo[n] = conteo [n] + 1 

print(conteo)


# 2 suma
datos = [("ana", 10), ("juan", 20), ("ana", 30), ("ana", 100)]

suma = {}


for clave, valor in datos:
    if clave not in suma:
        suma[clave] = 0
    
    suma[clave] +=  valor
print(suma)


# 3 agrupación

datos = [("ana", 10), ("juan", 20), ("ana", 30), ("juan", 5)]

agrupacion = {}

for clave, valor in datos:
    if clave not in agrupacion:
        agrupacion[clave] = []

    agrupacion[clave].append(valor)
print(agrupacion)