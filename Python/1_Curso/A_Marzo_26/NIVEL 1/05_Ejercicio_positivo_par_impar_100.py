numero=int(input ("Introduce un número:"))
if numero < 0:
   signo="negativo"
elif numero > 0:
     signo="positivo"
else:
    signo="cero"

if numero <= 100:
   tamaño="pequeño"
else:
    tamaño="grande"

if numero %2 ==0:
    paridad="par"
else:
    paridad="impar"
print(f"El número; {numero} es {signo},{paridad} y {tamaño}")



