# ordena por nota de menor a mayor y por nombre en caso de empate
alumnos =[{"nombre": "Mario", "nota": 7},
          {"nombre": "Lucia", "nota": 9},
          {"nombre": "Ana", "nota": 7},
          {"nombre": "Pedro", "nota": 5}]

ordena = sorted(alumnos, key=lambda x: (x["nota"], x["nombre"]))
print(ordena)