datos = (12, 5, 18, 3, 25, 7, 9, 8, 5)

# imprime números mayores que 10
for n in datos:
    if n > 10:
        print(n)

# dime cuantos números hay mayores que 10
contador = 0
for n in datos:
    if n > 10:
        contador +=1

print(f"Hay {contador} números mayores que 10")

# busca el número mayor
mayor = datos[0]
for n in datos:
    if n> mayor:
        mayor = n

print(mayor)

#sumas los números en posiciones pares del índice.
suma_par = 0
contador = 0
for n in datos:
    if contador %2 == 0:
        suma_par += n
        
    contador +=1    

print(suma_par)


#imprime los 3 primeros elementos y los tres últimos

contador_inicio = 0
contador_final = len(datos)-3

while contador_inicio < 3:
    print(datos[contador_inicio])
    contador_inicio += 1

while len(datos) > contador_final:
    print(datos[contador_final])
    contador_final += 1

# con SLICING
print(datos[:3])
print(datos[-3:])



# imprimir la tupla al reves
longitud = len(datos)-1

while longitud > -1:
    print(datos[longitud])
    longitud -=1

# con SLICING
print (datos[::-1])


# desempaquetado parcial (imprime el primer valor en a, el segundo en b, y el resto en una lista llamada resto)
a, b, *resto = datos
print(a,b,resto)


#contar ocurrencias


buscar = 2
congluencias = 0

for n in datos:
    if n == buscar:
        congluencias += 1

print(congluencias)


#comprueba si todos los números son mayores que 0
i = True
for n in datos:
    if n <= 0:
        i = False
    
if i == True:
    print("True")
else:
    print("False")

