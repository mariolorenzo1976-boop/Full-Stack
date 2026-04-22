numero =int(input ("Introduce un número:"))
paridad = numero %2
if numero < 0 and paridad == 0:
    print(f"el Número : {numero} es negativo y par")
elif numero < 0 and paridad ==1:
    print(f"el Número : {numero} es negativo e impar")
elif numero > 0 and paridad ==0:
    print(f"el Número : {numero} es positivo y par")
elif numero > 0 and paridad ==1:
    print(f"el Número : {numero} es positivo e impar")
else:
    print(f"el Número : {numero} es cero")

    