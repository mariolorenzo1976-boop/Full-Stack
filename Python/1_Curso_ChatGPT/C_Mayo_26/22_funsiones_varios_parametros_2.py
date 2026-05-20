# Ejercicio 1 - filtra por varios parámetros. por límite, y tipo



def filtra(datos, limite, tipo):

    resultado = []
    for n in datos:
        if tipo == "mayor" and n > limite:
            resultado.append(n)
        
        if tipo == "menor" and n < limite:
            resultado.append(n)

    return resultado
            




# Ejercicio 2 - Ordena de mayor a menor o de menor a mayor según se pida.

def ordena(datos, reverso):
        
    
    if reverso == True:
        resultado = sorted(datos, key=lambda x: -x)

    if reverso == False:
        resultado = sorted(datos, key=lambda x: x)
    
    return resultado




datos = [10, 40, 60, 90]
print(filtra(datos, 50, 'mayor'))
print(filtra(datos, 50, 'menor'))
print(ordena(datos, False))
print(ordena(datos, True))