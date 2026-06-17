# Ejercicio 1 funsión que devuelve máximo y mínimo

# Ejercicio 2 funsión que devuelve cantidad de valores y suma de los mismos

datos = [10, 40, 60 ,90]

datos_2 = [("bici", 100),
         ("run", 30),
         ("bici", 50),
         ("swim", 70)]

def max_min(datos):

    maximo = max(datos)
    minimo = min(datos)

    return maximo, minimo



def cantidad_suma(datos):

    cantidad = len(datos)
    suma = sum(datos)

    return cantidad, suma


def total_cantidad(datos_2, clave):

    total_veces = 0
    suma_km = 0
    for deporte, km in datos_2:
        if deporte == clave:
            total_veces +=1
            suma_km += km

    return total_veces, suma_km




maximo, minimo = max_min(datos)

print(maximo, minimo)


c, s = cantidad_suma(datos)
resultado_2 = (c, s)
print(resultado_2)


t, s = total_cantidad(datos_2, 'bici')
resultado_3 = (s, t)
print(resultado_3)