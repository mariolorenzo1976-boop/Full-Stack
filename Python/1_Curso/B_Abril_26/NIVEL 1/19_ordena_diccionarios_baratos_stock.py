# ordena los productos más baratos primero, y si cuestan lo mismo, que aparezcan los que más stock tienen.
productos = [{"nombre": "bici", "precio": 1200, "stock":5},
             {"nombre": "casco", "precio": 80, "stock":20},
             {"nombre": "ruedas", "precio": 300, "stock":10},
             {"nombre": "guantes", "precio": 80, "stock":50},]

ordena = sorted(productos, key=lambda x: (x["precio"], -x["stock"]))
print(ordena)