
#En este ejercicio vamos a filtrar, ordenar y clasificar+transformar una lista (if,sorted,else if)

#aquí solo estoy filtrando las rutas de más de 25 km usamos if
ruta = [
        {"nombre": "Teide", "km": 45, "desnivel": 1200},
        {"nombre": "Anaga", "km": 30, "desnivel": 900},
        {"nombre": "Costa", "km": 25, "desnivel": 200},
        {"nombre": "Norte", "km": 50, "desnivel": 1500}
        ]

mas_25 =[n for n in ruta if n["km"]>25]


# aquí estoy ordenando la lista por desnivel
ordenada = sorted(mas_25, key=lambda n: n["desnivel"], reverse=True)


#aquí solo estoy clasificando + transformando las rutas: usamos else if
clasificar = [f"{n['nombre']}: dura" 
              if n['desnivel']>1000 else 
              f"{n['nombre']}: media" if n['desnivel']>=500 else
              f"{n['nombre']}: suave"
              for n in ordenada
              ]

print(clasificar)