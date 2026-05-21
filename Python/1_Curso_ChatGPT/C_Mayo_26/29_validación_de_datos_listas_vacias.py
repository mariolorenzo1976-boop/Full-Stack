
# Ejercicio 1 valida la entrada de una lista vacia para la suma de todos los km

# datos = [("bici", 100),
#          ("run", 30),
#          ("bici", 50),
#          ("swim", 70),
#          ("run", 20)]

datos =[]

def suma_km(datos):
    
    total_km = 0
    
    if len(datos) == 0:
        return 0
    else:
        for clave, valor in datos:
            total_km += valor

        return total_km





# Ejercicio 2 valida la entrada de una lista vacia para el deporte con más km

def deporte_mas_km(datos):

    dep_mas_km = {}
    km = 0
    deporte = " "
    
    if len(datos) == 0:
        return None
    else:

        for clave, valor in datos:
            if clave not in dep_mas_km:
                dep_mas_km[clave] = 0
                
            dep_mas_km[clave] += valor

        for n in dep_mas_km:
            if dep_mas_km[n] > km:
                km = dep_mas_km[n]
                deporte = n
    

    return deporte





# Ejercicio 3 valida la entrada de una lista vacia para media_global de los deportes

def media_global(datos):

    media = 0
    suma = suma_km(datos)
    cantidad = len(datos) 
    if len(datos) == 0: 
        return 0
    else:
         media = suma / cantidad
         return media
       

print(suma_km(datos))
print(deporte_mas_km(datos))
print(media_global(datos))