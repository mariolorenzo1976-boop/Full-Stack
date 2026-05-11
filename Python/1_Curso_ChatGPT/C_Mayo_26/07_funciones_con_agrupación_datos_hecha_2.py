
datos = {'bici': [100, 50], 'run': [20]}

nuevo_diccionario = {"total":0, "count":0}

for n in datos:
    
    nuevo_diccionario[n] = sum(datos[n]) 

print(nuevo_diccionario)