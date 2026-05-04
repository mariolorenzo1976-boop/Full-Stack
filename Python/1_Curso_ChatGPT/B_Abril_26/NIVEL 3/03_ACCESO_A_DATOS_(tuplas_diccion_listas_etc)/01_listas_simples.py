
# recorremos una lista con un bucle for y mostramos cada elemento de la lista. En este caso, la lista es numeros, y cada elemento
numeros = [10, 20, 30, 40, 50]
for n in numeros:
    print(n)


# sumamos los elementos de la lista numeros, recorriendola con un bucle for, y guardando el resultado en una variable llamada suma, que se va actualizando en cada iteración del bucle. Al final, imprimimos el resultado de la suma.
suma = 0
for n in numeros:
    suma += n
print(suma)


# contamos el número de elementos de la lista numeros, recorriendola con un bucle for, y guardando el resultado en una variable llamada contador, que se va actualizando en cada iteración del bucle. Al final, imprimimos el resultado del contador.
contador = 0
for n in range (len(numeros)):
    contador += 1
print(contador) 


# contamos el número de elementos de la lista numeros, utilizando la función len(), que devuelve el número de elementos de la lista. Guardamos el resultado en una variable llamada variable, y lo imprimimos.
variable = len(numeros)
print(variable) 

# recorremos la lista numeros con un bucle for, y mostramos solo los elementos que son mayores que 25. Para ello, utilizamos una estructura condicional if dentro del bucle for, que evalúa si el elemento n es mayor que 25, y si es así, lo imprime.
for n in numeros:
    if n > 25:
        print(n)