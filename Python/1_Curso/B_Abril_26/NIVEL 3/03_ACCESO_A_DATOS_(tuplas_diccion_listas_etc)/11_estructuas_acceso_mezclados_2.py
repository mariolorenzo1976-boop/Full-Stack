# suma todos los números
datos = ((10, 20),(5, 15),(30, 40))

suma = 0
for n in datos:
    for tupla in n:
        suma  += tupla

print(suma)



# imprime solo las claves cuyo valor sea mayor que 25
datos = {"bici": 30, "run": 20, "swim": 40, "walk": 10}

for n in datos.values():
    if n > 25:
        print(n)

# imprime los nombres de personas con edad mayor o igual a 25
dato = [{"nombre": "Ana", "edad": 25},
        {"nombre": "Luis", "edad": 30},
        {"nombre": "Marta", "edad": 20}]

for n in dato:
   if n['edad'] >= 25:
       print(n['nombre'])


# Calcula la suma de todos los números
datos = (10, (20, 30), (5, 5), 40)

suma = 0
for n in datos:
    if isinstance (n, int):
        suma += n
    if isinstance (n, tuple):
        for tupla in n:
            suma += tupla

print(suma)

# imprime el nombre del deporte con mayor tiempo
datos = [("bici", 30), ("run", 50), ("swim", 40)]

nombre = ""
mayor = 0 
for n in datos:
    if n[1] > mayor:
       mayor = n[1]
       nombre = n[0]

print(nombre)



