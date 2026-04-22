# ordena por edad
personas = [("Ana", 30), ("Luis", 25), ("Carlos", 35)]
ordena_edad = sorted(personas, key=lambda x: x[1])
print(ordena_edad)
