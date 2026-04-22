

# ordena las palabras por longitud y alfabéticamente

palabras=["sol","casa","avión","perro","luz"]

ordena_palabras=sorted(palabras, key=lambda x: (len(x), x))


print(ordena_palabras)