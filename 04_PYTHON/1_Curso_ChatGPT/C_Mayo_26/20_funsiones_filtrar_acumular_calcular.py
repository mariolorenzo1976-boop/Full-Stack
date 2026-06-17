# Ejercicio 20 - devuelve solo pares (filtrado), suma todos los elementos, acumula los datos con la misma clave.


def pares(datos):
    
    pares=[]
    for clave, valor in datos:
        if valor % 2 == 0:
            pares.append([clave,valor])

    return pares 



def suma(datos):

    suma = 0
    for clave, valor in datos:
        suma += valor
    
    return suma


def acumulador(datos):

    acumla_datos={}
    for clave, valor in datos:
        if clave not in acumla_datos:
            acumla_datos[clave] = 0

        acumla_datos[clave] += valor  
    
    return acumla_datos


datos = [("bici", 100), ("run", 30), ("bici", 50)]
pares = pares(datos)
suma = suma(datos)
acumula_datos = acumulador(datos)
print(pares, suma, acumula_datos)



