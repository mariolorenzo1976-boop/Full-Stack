# #devuelve solo la ruta con mayor desnivel
# #texto
# #formato nombre (1500)

rutas =[{"nombre": "Teide", "km":45, "desnivel": 1200},
        {"nombre": "Anaga", "km":30, "desnivel": 900},
        {"nombre": "Costa", "km":25, "desnivel": 200},
        {"nombre": "Norte", "km":50, "desnivel": 1500}
        ]

# sacamos la ruta con mallor desnivel usando max
mayor_desnivel = max(rutas, key=lambda x: x['desnivel'])
# formateamos para sacar por pantalla
ruta_mayor_desnivel = f"{mayor_desnivel['nombre']} ({mayor_desnivel['desnivel']})" # Devuelve un string, entre corchetes devuelve una lista
# mostramos el resultado formateado
print(ruta_mayor_desnivel)






#-------------- EJERCICIO MAL HECHO DEBAJO : CORRECCIÓN ARRIBA--------------------








# rutas =[{"nombre": "Teide", "km":45, "desnivel": 1200},
#         {"nombre": "Anaga", "km":30, "desnivel": 900},
#         {"nombre": "Costa", "km":25, "desnivel": 200},
#         {"nombre": "Norte", "km":50, "desnivel": 1500}
#         ]

# mayor_desnivel = [f"{n['nombre']} ({n['desnivel']})" for n in rutas]

# mayor_des=[]

# mayor = rutas["desnivel"]
# print(mayor)



# # for n in rutas:
# #     if mayor > rutas['desnivel']:
# #         mayor = rutas['desnivel']

# # print(rutas[mayor])



# # la_mayor = max(mayor_desnivel,key=lambda n: n['desnivel'])
# # print(la_mayor)

