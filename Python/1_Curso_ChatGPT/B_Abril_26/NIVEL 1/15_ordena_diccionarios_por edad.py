# ordena por edad
personas = [
            {"nombre": "Ana", "edad": 30},
            {"nombre": "Luis", "edad": 25},
            {"nombre": "Carlos", "edad": 35}
            ]

ordena = sorted(personas,key=lambda x: x["edad"])
print(ordena)
