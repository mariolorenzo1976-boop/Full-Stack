
# ----------------- LISTAS -----------------------#


# cuenta cuantas veces se repite
datos = ["bici", "run", "bici"]

contador= 0

for clave in datos:
    if clave == "bici":
        contador +=1


# suma todos los datos

datos = [10, 20, 30]

suma = 0
for clave in datos:
    suma += clave


# acumuladores
# acumula los valores para la misma clave
datos = [("bici", 100), ("run", 20), ("bici", 50)]

diccionario = {}

for clave, valor in datos:
    if clave not in diccionario:
        diccionario[clave] = 0
    diccionario[clave] += valor

print(diccionario)


# agrupación
# agrupa los valores para la misma clave
datos = [("bici", 100), ("run", 20), ("bici", 50)]

lista = {}

for clave, valor in datos:
    if clave not in lista:
        lista[clave] = []
    lista[clave].append(valor)

print(lista)


# funsiones
# suma los valores para la misma clave

def suma_lista(datos):

    suma = 0
    for n in datos:
        suma += n
    
    return(suma)

     
datos = [10, 20, 30]
print(suma_lista(datos))


# funsiones integradas
datos = [10, 20, 5, 40]

print(sum(datos))
print(max(datos))
print(min(datos))
print(len(datos))

# calcula el promedio de cada clave sin sum()

datos = {'bici': [100, 50], 'run': [20]}

datos_promedio = {}

for clave, valor in datos.items():
    suma = 0
    if clave not in datos_promedio:
        datos_promedio[clave] = 0
        promedio = 0
        for n in valor:
            suma += n
            promedio +=1
        datos_promedio[clave] = suma / promedio
print(datos_promedio)


datos = (100, 200, 300, 400, 500)
datos_2 = (1000, 2)


datos_3 = datos + datos_2

print(datos_3)

    

