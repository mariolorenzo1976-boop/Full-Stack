datos = (10, 20, 30, 40 ,50, 9)


# Recorrer tupla
for n in datos:
    print(n)

# imprimir primer elemento y el último
contador = len(datos) - 1
print(datos[0])
print(datos[contador])

# otra forma de primer elemento y el último. para Python el -1 es el último elemento
print(datos[0])
print(datos[-1])

# suma todos los datos en tuplas
contador = 0
suma = 0
for n in datos:
    suma += datos[contador]
    contador += 1

print(suma)

#otra forma de sumar mejor
sumar = 0
for n in datos:
    sumar += n

print(sumar)


# contar elementos sin len
contador = 0
for n in datos:
    contador += 1
print(f"hay {contador} elementos")


# Buscar elementos, comprueba si existe el elemento 9
existe = False
for n in datos:
    if n == 9:
        existe = True
        
if existe == True:
    print("existe")
else:
    print("No existe")


