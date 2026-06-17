# Ejercicio 13 - acumulador + conteo
datos = [
    ("ana", 10),
    ("juan", 20),
    ("ana", 30),
    ("juan", 5),
    ("ana", 15)
]

conteo = {} 

for clave, valor in datos:
    if clave not in conteo:
       conteo[clave] = {"total":0, "count":0}

    
    conteo[clave]["total"] += valor
    conteo[clave]["count"] += 1
                   
print(conteo)  
    
