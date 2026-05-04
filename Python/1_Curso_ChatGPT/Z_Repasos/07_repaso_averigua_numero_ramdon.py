import random

numero=random.randint(1, 100)
dato=0
while dato != numero:
    dato = int(input("Acierta que número estoy pensando:"))
    if dato < numero:
        print ("El número es mayor")
    elif dato > numero:
        print ("El número es menor")

print("correcto")