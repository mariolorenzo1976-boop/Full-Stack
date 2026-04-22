# ordena por nota, si hay empate por nombre de los empatados
alumnos = [("Mario", 7), ("Lucia", 9), ("Ana", 7), ("Pedro", 5)]
ordena = sorted(alumnos, key=lambda x: (x[1], x[0]))
print(ordena)