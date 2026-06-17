

# ordena precio (menor a mayor) y si hay empate, por nombre alfabéticamente

productos=[("bici",1200),("casco",80),("ruedas",300),("guantes",80)]

ordena_productos=sorted(productos, key=lambda x: (x[1],x[0])) # en este caso x1 pertenece al segundo dato de los registros, y x0 pertenece al primer dato de los registros

print(ordena_productos)