# 1 crea una lista con nº al cuadrado
datos = [1, 2, 3, 4, 5]

resutltado = [x ** 2 for x in datos]

print(resutltado)

# 2 solo números mayores que 10
datos = [1, 4, 9, 16, 25]

resultado = [x for x in datos if x > 10]

print(resultado)

# 3 extrae los nombres
datos= [("a", 1), ("b", 2), ("c", 3)]

resultado = [x[0] for x in datos]

print(resultado)

# 4 extrae solo valores
datos = {"a": 10, "b": 2, "c": 3}

resultado = [y for x, y in datos.items()]

print(resultado)

# 5 aplana la lista de tuplas
datos = ((1, 2), (3, 4), (5, 6))

resultado = [y for x in datos for y in x]

print(resultado)

# 6 solo pares y multiplicados por 10
datos = [1, 2, 3, 4, 5, 6]

resultado = [x * 10 for x in datos if x %2 == 0]

print(resultado)

# 7 Extrae solo los segundos valores
datos= [("a",10), ("b",20), ("c",30)]

resultado = [x[1] for x in datos]

print(resultado)

