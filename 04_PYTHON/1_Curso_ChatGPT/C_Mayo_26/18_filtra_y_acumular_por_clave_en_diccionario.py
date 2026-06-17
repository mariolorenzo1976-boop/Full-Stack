# Ejercicio 18 - filtra y acumula solo los valores mayores a 15

datos = [
    ("bici", 10),
    ("run", 20),
    ("bici", 30),
    ("swim", 5),
    ("run", 50),
    ("bici", 15)
]

valores_filtrados = []
for clave, valor in datos:
    if valor >= 15:
        valores_filtrados.append((clave,valor))

print(valores_filtrados)

acumulados = {}
for clave, valor in valores_filtrados:
    if clave not in acumulados:
        acumulados[clave] = []

    acumulados[clave].append(valor)

print(acumulados)

sumados = {}
for clave, valor in acumulados.items():
    sumados[clave] = sum(valor)

print(sumados)