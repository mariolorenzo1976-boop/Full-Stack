# ordena esta lista por nombre de Z_A y si hay empate, precio de menor a mayor
productos = [{"nombre" : "bici" , "precio" : 1200},
             {"nombre" : "casco" , "precio" : 80},
             {"nombre" : "ruedas" , "precio" : 300},
             {"nombre" : "guantes" , "precio" : 80},
             {"nombre" : "zapatillas" , "precio" : 120} ]

productos.sort(key=lambda x: x["precio"])
productos.sort(key=lambda x: x["nombre"], reverse=True)

print(productos)