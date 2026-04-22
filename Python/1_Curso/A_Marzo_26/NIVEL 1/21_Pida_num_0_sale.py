numero=[]
dato=1
suma=0
media=0
contador=0


while dato !=0:
    dato=int(input("introduce un número, el 0 sale:"))
    if dato !=0:
        numero.append(dato)
        suma=suma+dato
        contador +=1
        media= suma/contador

if contador !=0:
    mayor=numero[0]
    menor=numero[0]       
    for numeros in range(len(numero)):
        if mayor<numero[numeros]:
            mayor=numero[numeros]
        if menor>numero[numeros]:
            menor=numero[numeros]
    print(f"El dato menor es:{menor} , y el mayor es: {mayor}")

print(numero)
print(f"la suma de la lista es:{suma}")
print(f"La media de la lista es:{media}")
#print(f"El dato menor es:{menor} , y el mayor es: {mayor}")

