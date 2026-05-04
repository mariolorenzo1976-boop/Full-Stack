#modificar precio del casco en 100€
productos = [{"nombre": "bici", "precio": 1200, "stock":5},
             {"nombre": "casco", "precio": 80, "stock":20},
             {"nombre": "ruedas", "precio": 300, "stock":10},
             {"nombre": "guantes", "precio": 80, "stock":50},]

for producto in productos:
    if producto["nombre"] == "casco":
        producto["precio"] = 100

print(productos)