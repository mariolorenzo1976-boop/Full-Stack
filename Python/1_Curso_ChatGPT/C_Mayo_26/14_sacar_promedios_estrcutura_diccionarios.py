# Ejercicio 14 - promedio con estructura de diccionarios

conteo = {
    'ana': {'total': 55, 'count': 3},
    'juan': {'total': 25, 'count': 2}
}

resultado = {}
for clave, valor in conteo.items():
    
    resultado [clave] = conteo[clave]["total"] / conteo[clave]["count"]

print (resultado)