numeros = []
a = 1

for i in range(5):
    dato = int(input(f"introduce el {a}º número de cinco números:"))
    numeros.append(dato)
    a +=1

print(f"Los números introducidos son: {numeros}")
print(f"El número mayor es: {max(numeros)}")
print(f"El número menor es: {min(numeros)}")


