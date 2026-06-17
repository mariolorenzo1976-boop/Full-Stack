# acumulador guardado en diccionarios: con 1 clave, si no existe en el diccionario lo creo, sino lo acumulo
datos = ["bici", "bici", "bici"]

resultado= {}

for n in datos:
    if n == "bici":
       if n not in resultado: # si no existe en diccionario
           resultado[n] = 0. # lo creo
       resultado[n] += 1  # sinó, lo acumulo

print(resultado)




# acumulador con 2 claves
datos = ["bici", "run", "bici", "run", "bici"]

resultado = {}

for n in datos:
    if n not in resultado:
        resultado[n] = 0
    resultado[n] += 1

print(resultado) 


# acumulador con valores
datos = [("bici", 100), ("run", 30), ("bici", 50)]

resultado= {}

for clave, valor in datos:
    if clave not in resultado:
        resultado[clave]=0
    resultado[clave] += valor

print(resultado)
