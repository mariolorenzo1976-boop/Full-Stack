
# Ejercicio 1 devuelve la suma de los km, y verifica si la lista esta vacia y los número no son string

datos = [("bici",100), ("run",30)]

datos = [("bici", "hola")]

def suma_km(datos):

    km = 0
    if len(datos) == 0:
        return 0
    else:
        for clave, valor in datos:
            if isinstance(valor, (int, float)) == False:
                return 0
            else:
                km += valor
        return km
                
print(suma_km(datos))

# Ejercicio 2 media global solo con los valores correctos


datos = [("bici","hola"), ("run",30)]


def media_global(datos):

    suma_kms = 0
    contador = 0
    if len(datos) == 0:
        return 0
    else:
        for clave, valor in datos:
            if isinstance(valor, (int,float)) == True:
                suma_kms += valor
                contador += 1

        if suma_kms == 0 or contador == 0:
            return 0
        else:
            return suma_kms / contador
            



print (media_global(datos))

