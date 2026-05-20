# Ejercicio 26 devuelve esto: el total de km por deporte y cuantas veces se repite el deporte 
# {'bici': {'total': 150, 'veces': 2}, 
#  'run': {'total': 50, 'veces': 2}, 
#  'swim': {'total': 70, 'veces': 1}}

datos = [("bici", 100),
         ("run", 30),
         ("bici", 50),
         ("swim", 70),
         ("run", 20)]


def km_veces(datos):

    
    deporte = {}
    for clave, valor in datos:
        if clave not in deporte:
            deporte[clave] = {"total": 0, "veces": 0}

        deporte[clave]["total"] += valor
        deporte[clave]["veces"] += 1

    return deporte

print(km_veces(datos))    