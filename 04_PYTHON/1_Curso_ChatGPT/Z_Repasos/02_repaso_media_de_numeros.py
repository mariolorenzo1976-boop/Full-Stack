numeros = []
sumatorio = 0
contador = 0
dato = 1
media = 0
while dato !=0:
    dato = int(input("Introduce números hasta la salida 0:"))
    if dato != 0:
        numeros.append(dato)
        sumatorio = sumatorio + dato
        contador +=1
if len(numeros) !=0:
    media = sumatorio / contador

print(f"Los números introducidos son {numeros}, y la media {media}")
