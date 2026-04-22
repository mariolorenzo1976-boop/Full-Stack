# ordena la lista por precio de menor a mayor, y por nombre
productos = [("bici", 1200),
             ("casco", 80),
             ("ruedas", 300),
             ("guantes", 80),
             ("zapatillas", 120),]

ordenados = sorted(productos, key=lambda x: (x[1], x[0]))

print(ordenados)