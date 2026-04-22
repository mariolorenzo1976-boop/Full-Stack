# devuelve la ruta con menor desnivel
# formato nombre (desnivel)
ruta =[{"nombre": "Teide", "km": 45, "desnivel":1200},
       {"nombre": "Anaga", "km": 30, "desnivel":900},
       {"nombre": "Costa", "km": 25, "desnivel":200},
       {"nombre": "Norte", "km": 50, "desnivel":1500},
       {"nombre": "Sur", "km": 20, "desnivel":300},]

# lo realizamos con un bucle normal
menor = ruta[0]

for n in ruta:
    if n["desnivel"] < menor["desnivel"]:
        menor = n

resultado = f"{menor['nombre']} ({menor['desnivel']})"

print(resultado)



# lo realizamos con list compreshion
# primero localizamos en la lista el menor desnivel
desnivel_menor = min(ruta, key=lambda x: x['desnivel'])
# luego aplicamos el formato de salida
ruta_menor = f"{desnivel_menor['nombre']} ({desnivel_menor['desnivel']})"

print(ruta_menor)