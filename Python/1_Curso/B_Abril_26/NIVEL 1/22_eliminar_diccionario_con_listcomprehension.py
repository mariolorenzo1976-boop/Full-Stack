# elimina un producto sin stock con listcomprehension
productos = [{"nombre": "bici", "precio": 1200, "stock":5},
             {"nombre": "casco", "precio": 80, "stock":20},
             {"nombre": "ruedas", "precio": 300, "stock":0},
             {"nombre": "guantes", "precio": 80, "stock":50},]

productos = [p for p in productos if p["stock"] >0]
print(productos)
