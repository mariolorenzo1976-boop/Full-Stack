# elimina los impares
lista = [1, 2, 3, 4, 5, 6, 7]
lista_par=[]


i=0

while i < len(lista):
    if lista[i] %2 == 0:
        lista_par.append(lista[i])
        
    i+=1
    

print(lista_par)