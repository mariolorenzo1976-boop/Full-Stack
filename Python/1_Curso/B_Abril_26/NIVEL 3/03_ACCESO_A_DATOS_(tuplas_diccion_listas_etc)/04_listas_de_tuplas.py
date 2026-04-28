datos = [("bici",3), ("running",10), ("swim",13)]

# sumamos los valores de la tupla, es decir la segunda posición de cada elemento. El índice es 1 porque el primer elemento empieza en 0

suma = 0
for n in datos:
    suma += n[1]

print(suma)


valor = 0
for n in datos:
    if n[1] > valor:
        valor = n[1]

print(f"el valor mayor es: {valor}")