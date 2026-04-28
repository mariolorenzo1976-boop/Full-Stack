datos = [{"deporte": "bici", "tiempo": 30},
         {"deporte": "running", "tiempo": 20},
         {"deporte": "swim", "tiempo": 40}

]


# imprime todos los deportes
for n in datos:
    print(n["deporte"])


# suma de todos los tiempos
suma = 0
for n in datos:
    suma += n["tiempo"]

print(suma)

# imprime el deporte con más tiempo
mas_tiempo = 0
deporte = ""
for n in datos:
    if n['tiempo'] > mas_tiempo:
        mas_tiempo = n["tiempo"]
        deporte = n["deporte"]

print("el deporte con más tiempo es", deporte)