
contador=0
datos=[]
valor=0
suma=0
positivos=0
while contador<5:
    valor=int(input("introduce un número:"))
    datos.append(valor)
    contador +=1
    suma=suma+valor
    if valor >= 0:
        positivos +=1


#for numero in contador:
print(datos) # Muestra la lista completa
print(suma)
print(f"Hay {positivos} , números positivos")

#Forma de averiguar que datos es mayor o menor, programando
mayor=datos[0]
menor=datos[0]
for i in range(len(datos)):
    
    if mayor<datos[i]:
       mayor=datos[i]
    
    if  menor>datos[i]:
        menor=datos[i]

print(f"el número mayor de la lista es: {mayor}")
print(f"el número menor de la lista es: {menor}")

#Forma de averiguar que datos es mayor o menor, con las funsiones de phyton

mayor=max(datos)
menor=min(datos)
print(f"el número mayor de la lista es: {mayor}")
print(f"el número menor de la lista es: {menor}")

