productos = [("bici",1200), 
             ("casco",80),
             ("ruedas",300),
             ("guantes",80)]

ordenada_precios = sorted(productos, key=lambda x: (x[1], x[0]))

print(ordenada_precios) 