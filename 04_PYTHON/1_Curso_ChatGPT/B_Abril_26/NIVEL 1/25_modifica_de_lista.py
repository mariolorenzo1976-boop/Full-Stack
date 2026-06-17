# modifica la posición 3 por 10
lista = [1, 2, 3, 4, 5, 6, 7]

x=len(lista)
i=0
while i < x:
    if lista[i]==3:
        lista[i]=10
    i +=1

print(lista)