# Ejercicio 17 - fusión con varios parámetros
def numeros_mayores(datos, numero):
    
    mayores = []

    for n in datos:
        if n > int(numero):
           mayores.append(n) 

    return mayores


datos = [10, 50, 20, 80, 5, 35]

numero = input("introduce un número para filtrar mayores:")

resultado = numeros_mayores(datos,numero)
print("Los números mayores son:", resultado)
