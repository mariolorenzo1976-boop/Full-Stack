# ordena por precio descendente y stock ascendente

productos = [{"nombre": "teclado", "precio": 50, "stock": 10},
             {"nombre": "raton", "precio": 20, "stock": 50},
             {"nombre": "monitor", "precio": 150, "stock": 5},
             {"nombre": "altaboces", "precio": 60, "stock": 30}]

ordena = sorted(productos, key=lambda x: (-x["precio"], x["stock"]))

print(ordena)