# ordena los productos por precio de menor a mayor
productos = [{"nombre" : "bici", "precio" : 1200},
             {"nombre" : "casco", "precio" : 80},
             {"nombre" : "ruedas", "precio" : 300},
             {"nombre" : "guantes", "precio" : 80},
             {"nombre" : "zapatillas", "precio" : 120}]


ordenado = sorted(productos, key=lambda x: x["precio"])
print(ordenado)