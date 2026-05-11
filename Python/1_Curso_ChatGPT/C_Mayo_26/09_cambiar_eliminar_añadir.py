# añadir, modificar y eliminar de la lista

datos = ["bici", "run", "swim", "run"]

# modificar dato "run" por "trail"
datos[1] = "trail"
print(datos)

# eliminamos el primer "run"
datos.pop(2)
print(datos)

# añadimos "gym" a la lista
datos.append("gym")
print(datos)