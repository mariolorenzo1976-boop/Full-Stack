# acumula en lista los valores de las misma clave

def acumulador(datos):

    resultado={}

    for clave, valor in datos:
        if clave not in resultado:
            resultado[clave] =[]
        resultado[clave].append(valor)
    
    return(resultado)


datos = [("bici", 100), ("run", 20), ("bici", 50)]
resultado = acumulador(datos)
print(resultado)
