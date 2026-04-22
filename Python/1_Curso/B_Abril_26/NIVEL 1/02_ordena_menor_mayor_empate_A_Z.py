# ordena la lista por nombre de Z-A y Precio (de menor a mayor)

productos = [("bici", 1200),
             ("casco", 80),
             ("ruedas", 300),
             ("guantes", 80),
             ("zapatillas", 120)]

#ordenamos en 2 pasos con sort
productos.sort (key=lambda x: x[1]) #ordenar por precio (menor a mayor)
productos.sort (key=lambda x: x[0], reverse=True) # ordena por nombre (Z-A)


print(productos)
             