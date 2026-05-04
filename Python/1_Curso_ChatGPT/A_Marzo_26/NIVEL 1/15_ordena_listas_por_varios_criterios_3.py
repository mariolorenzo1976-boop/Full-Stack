

# ordena las palabras por última letra y longitud

palabras=["coche","avión","barco","tren","sol"]

ordena_palabras=sorted(palabras, key=lambda x: (x[-1], len(x)))

print(ordena_palabras)

