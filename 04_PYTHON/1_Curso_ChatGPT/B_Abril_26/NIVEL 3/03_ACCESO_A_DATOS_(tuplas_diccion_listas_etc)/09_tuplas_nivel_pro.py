# #imprime el segundo número mayor

# datos = (12, 5, 18, 3, 25, 7, 25, 9)

# primer_mayor = float ('-inf')
# segundo_mayor = float ('-inf')

# for n in datos:
#     if n > primer_mayor:
#         primer_mayor = n
        
# for n in datos:
#     if n != primer_mayor and n > segundo_mayor:
#         segundo_mayor = n
    


# print(primer_mayor)
# print(segundo_mayor)    


# #cuantos números son pares y cuantos impares

# datos_2 = (4, 7, 10, 3, 6, 9, 2)

# pares = 0
# impares = 0

# for n in datos_2:
#     if n %2 == 0:
#         pares += 1
#     else:
#         impares += 1

# print(pares)
# print(impares)


# #suma solo los que estén en posiciones impares

# datos_3 = (10, 15, 20, 25, 30)

# suma_posicion_impar = 0
# contador = 0

# for n in datos_3:
#     if contador %2 != 0:
#         suma_posicion_impar += n
    
#     contador += 1

# print(suma_posicion_impar)


# #encuentra el primer número que se repite

# datos_4 = (3, 5, 7, 3, 9, 5)
# no_repe = []

# primer_repetido = False
# numero = 0

# for n in datos_4:
#     if n not in no_repe and primer_repetido == False:
#         no_repe.append(n)
       
#     else:    
#         numero = n
#         primer_repetido = True
#         break
    
    
# print("el primer número repetido es:", numero)


# # otra forma de encontrar el primer número repetido sin usar listas
# datos_4 = (3, 5, 7, 3, 9, 5)

# primer_repetido = None

# i = 0
# while i < len(datos_4):
#     j = i + 1
#     while j < len(datos_4):
#         if datos_4[i] == datos_4[j]:
#             primer_repetido = datos_4[i]
#             break
#         j += 1
#     if primer_repetido is not None:
#         break
#     i += 1

# print("El primer número repetido es:", primer_repetido)

# #imprimir solo los valores que no se repiten

# # datos_5 = (1, 2, 2, 3, 4, 4, 5)
# datos_5 = (1, 2, 3, 2, 3)

# lista_repe=[]
# i = 0
# repetido = False
# while i < len(datos_5):
#     j = i + 1
#     while j < len(datos_5) and repetido == False:
#         if datos_5[i] == datos_5[j]:
#            repetido = True
#            lista_repe.append(datos_5[i])
          
#         j = j + 1
    
#     repetido = False
#     i= i + 1

# for n in datos_5:
#     if n not in lista_repe:
#        print(n)
# print(lista_repe)

# #contar cuantas veces aparece cada número (evita salidas duplicadas), en este caso el conteo se hace hacia adelante.

# datos_6 = (1, 2, 2, 3, 1, 4)

# i=0
# veces = []
# contador = 1
# dato = 0
# repetidos=[]

# while i < len(datos_6):
#     j = i + 1
    
#     while j < len(datos_6):
#         if datos_6[i] == datos_6[j]:
                
#             contador += 1
            
#         j += 1
    
#     if datos_6[i] not in repetidos:
#         repetidos.append(datos_6[i])
#         veces.append((datos_6[i],contador))
#     i += 1
#     contador = 1
    
# i = 0
# j = 1
# for n in veces:
#     print(f"{n[i]} , se repite: {n[j]} veces")

# # imprimir cuantas veces aparece cada número comparando todos con todos en la lista (evita salidas duplicadas), en este caso el conteo se hace contra todos.
# datos_6 = (1, 2, 2, 3, 1, 4)

# i = 0
# j = 0
# vistos = []
# repetidos = []

# while i < len(datos_6):
#     j = 0
#     contador = 0
    
#     while j< len(datos_6):
#         if datos_6[i] == datos_6 [j]:
#            contador += 1
          
#         j += 1
    
#     if datos_6[i] not in vistos:
#         vistos.append(datos_6[i])
#         repetidos.append((datos_6[i], contador))
#     i += 1

# for n in repetidos:
#     print(f"{n[0]}, está repetido {n[1]} veces")


# #  suma todos los números de la tupla (aquí tenemos asumimos que la tupla tiene 2 datos)

# datos = ((1, 2), (3, 4), (5, 6))

# suma = 0
# for n in datos:
#     suma = suma + (n[0] + n[1])

# print(suma)
   


#  suma todos los números de la tupla (aquí tenemos asumimos que no sabemos la cantidad de datos de la tupla)

# datos = ((1, 2), (3, 4), (5, 6))

# tupla = 0
# suma = 0

# for n in datos:
#     while tupla < len(n):
#         suma = suma + n[tupla]
    
#         tupla += 1
#     tupla = 0
# print(suma)


# #  suma todos los números de la tupla (aquí tenemos asumimos que no sabemos la cantidad de datos de la tupla) con 2 for:

# datos = ((1, 2), (3, 4), (5, 6))
# suma = 0
# for n in datos:
#     for tupla in n:
#         suma = suma + tupla
    
# print(suma)


# # Encuentra el nº más grande en tupla anidada.

# datos = ((10, 2), (15, 8), (20, 1))

# mayor = float('-inf')
# for n in datos:
#     for tupla in n:
#         if tupla > mayor:
#             mayor = tupla
# print(mayor)


# # imprime solo los deportes cuyo tiempo sea mayor que 25

# datos = (("bici", 30), ("run", 20), ("swim", 40))


# for n in datos:
#     if n[1] > 25:
#        print(n[0])

# imprime solo los deportes cuyo tiempo sea mayor que 25 otra forma mejor

# datos = (("bici", 30), ("run", 20), ("swim", 40))

# for deporte, tiempo in datos:
#     if tiempo > 25:
#         print(deporte)



# encuentra el índice o posición del número mayor
datos = ((10, 3), (5, 8), (20,1))

n_mayor = float('-inf')

encontrado = False
indice = 0
contador = 0
for n in datos:
    for tupla in n:
       if tupla > n_mayor:
          n_mayor = tupla
          indice = contador
         
    
    contador +=1

print(indice)

