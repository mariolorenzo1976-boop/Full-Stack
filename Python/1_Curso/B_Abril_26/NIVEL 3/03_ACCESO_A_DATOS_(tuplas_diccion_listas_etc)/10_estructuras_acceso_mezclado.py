#Ejercicio 1: imprime números mayores de 25 de la lista

datos_lista = [10 ,20, 25, 35]

for n in datos_lista:
    if n > 25:
        print(n)



#Ejercicio 2: calcula la suma total de la tupla

datos_tupla = (5, 15, 25, 35)

suma = 0
for n in datos_tupla:
    suma += n

print(suma)


#Ejercicio 3: imprime solo los valores mayores que 25 en el diccionario

datos_diccionario = {"bici": 30, "run": 20, "swim": 40 }

for clave, valor in datos_diccionario.items():
    if valor > 25:
        print(clave)


#Ejercicio 4: imprime los valores con tiempos mayores a 25 en la lista de tuplas

datos_lista_tuplas = [("bici", 30), ("run", 20),("swim", 40)]

for n in datos_lista_tuplas:
    if n[1] > 25:
        print(n[0])


#Ejercicio 5: imprime los valores con tiempos mayores a 25 en la lista de diccionarios

datos_listas_diccionarios = [{"deporte": "bici", "tiempo": 30},
                             {"deporte": "run", "tiempo": 20},
                             {"deporte": "swim", "tiempo": 40}]

for n in datos_listas_diccionarios:
    if n['tiempo'] > 25:
        print(n["deporte"])


#Ejercicio 6: encuentra el número mayor en la tupla de tuplas

datos_tuplas_anidadas = ((10, 3), (5, 8), (1, 20))

suma = 0
for n in datos_tuplas_anidadas:
    for subtupla in n:
        suma += subtupla

print(suma)


#Ejercicio 7: imprime todos los deportes de diccionarios + listas

datos_dicc_listas = {"nombre": "Mario",
                     "deporte": ["bici", "run", "swim"]}

for clave, valor in datos_dicc_listas.items():
    if clave == "deporte":
        for n in valor:
            print(n)


            #Ejercicio 7: Mejor versión

    for deporte in datos_dicc_listas["deporte"]:
        print(deporte)






#Ejercicio 8: suma todos los números de la lista mixta

datos_listas_mixtas = [10 , (20, 30), [40 , 50]]


suma = 0
for n in datos_listas_mixtas:
    if isinstance(n, int):
        suma += n
    if isinstance(n, tuple):
        for x in n:
            suma += x
    if isinstance(n, list):
        for y in n:
            suma += y

print(suma)



