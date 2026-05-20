#Ejercicio 1 devuelve los enteros mayores que 50 , y los enteros menores que 50

datos = [10 ,25, 40, 60, 90]

#Ejercicio 2 devuelve en una lista los kilometros de un determinado deporte

datos_2 = [("bici", 100),
         ("run", 30),
         ("bici", 50),
         ("swim", 70)]

#Ejercicio 3 devuelve la media
datos_3 = [10 ,20, 30, 40, 50]


def mayor_menor(datos, limite, tipo):

    resultado = []
    for n in datos:
        if tipo == "mayor":
            if n > limite and n % 2 == 0:
               resultado.append(n)
        elif tipo == "menor":
            if n < limite and n % 2 == 0:
                resultado.append(n)
    return resultado

def km_deporte(datos_2, deporte):

    resultado_km = []
    for clave, valor in datos_2:
        if clave == deporte:
            resultado_km.append(valor)
    return resultado_km


def media(datos_3):

    
    resultado = sum(datos_3) / len(datos_3)
    return int(resultado)


print(mayor_menor(datos, 50, 'mayor'))
print(mayor_menor(datos, 50, 'menor'))

print(km_deporte(datos_2, 'bici'))

print(media(datos_3))






