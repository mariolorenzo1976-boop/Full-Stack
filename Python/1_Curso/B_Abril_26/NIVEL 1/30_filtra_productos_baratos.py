# filtra productos que cueste menos de 30
productos = [{"nombre": "camiseta", "precio": 20},
             {"nombre": "zapatillas", "precio": 80},
             {"nombre": "gorra", "precio": 15}
             ]

barato = [n for n in productos if n["precio"]<30]
print(barato)