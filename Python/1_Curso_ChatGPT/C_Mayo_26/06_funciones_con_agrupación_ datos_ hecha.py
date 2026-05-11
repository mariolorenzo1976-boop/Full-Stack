
# función que devuelve el promedio de un diccionario con agrupación de datos hecha

def promedio(datos):

    diccionario = {}
    promedio = 0
 

    for n in datos:
        suma_km = 0
        for km in datos[n]:
            suma_km += km
        diccionario[n] = suma_km / len(datos[n])
      

    return(diccionario)


datos = {'bici': [100, 50], 'run': [20]}

diccionario = promedio(datos)

print(diccionario) 


