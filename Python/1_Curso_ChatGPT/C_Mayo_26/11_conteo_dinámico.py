# 1 haz un conteo

datos =["bici", "run", "bici", "swim", "run", "bici", "bici", "run", "swim"]

conteo={}

for n in datos:
     if n not in conteo:
        conteo[n] = 0
        
     conteo[n] += 1
        
print(conteo)


# Haz un Filtrado de actividades >= 50

datos = [("bici", 100), ("run", 20), ("swim", 10), ("trail", 60)]

resultado=[]
for clave, dato in datos:
    if dato >= 50:
        resultado.append((clave, dato))

print(resultado)

# Agrupación

datos = [("bici", 100), ("run", 20), ("bici", 50), ("run", 30)]

contador = 0
nueva_lista = {}

for clave, valor in datos:
    if clave not in nueva_lista:
       nueva_lista[clave] = []

    nueva_lista[clave].append(valor)   

print(nueva_lista)

# funcion suma

def suma(datos):
    suma= 0 
    for n in datos:
        suma += n

    return suma
 

datos = [10 ,20, 30]
print(suma(datos))


    
    