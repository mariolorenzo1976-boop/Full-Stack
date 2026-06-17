# Ejercicio 19 - pasar ejercicio 18 a funsiones

def filtrados (datos):
    valores_filtrados = []
    for clave, valor in datos:
        if valor >= 15:
            valores_filtrados.append((clave,valor))

    return valores_filtrados

def acumulados (valores_filtrados):
    acumulados = {}
    for clave, valor in valores_filtrados:
        if clave not in acumulados:
            acumulados[clave] = []

        acumulados[clave].append(valor)

    return acumulados


def sumados (acumulados):
    sumados = {}
    for clave, valor in acumulados.items():
        sumados[clave] = sum(valor)

    return sumados


datos = [
    ("bici", 10),
    ("run", 20),
    ("bici", 30),
    ("swim", 5),
    ("run", 50),
    ("bici", 15)
]

datos_filtrados = filtrados(datos)
datos_acumulados = acumulados(datos_filtrados)
datos_sumados = sumados(datos_acumulados)

print("El resultado es:", datos_sumados)
