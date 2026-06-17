
# Ejercicio 1 - funsión datos menores que un número

def num_menores(datos, menor):
    
    resultado_menor = []
    for n in datos:
        if n < menor:
            resultado_menor.append(n)

    return resultado_menor



# Ejercicio 2 - funsión que devuelve la clave,  valor del la clave buscada.

def sport(datos_2,clave):

    #acumulador
    resultado_deporte = {}
    for deporte, distancia in datos_2:
        if deporte not in resultado_deporte:
            resultado_deporte[deporte] = 0
        resultado_deporte[deporte] += distancia

    #comparador
    resultado_final = []
    variable = ()
    for n in resultado_deporte:
        if n == clave:
            variable = n,resultado_deporte[n]
            resultado_final.append(variable)

    return resultado_final


# Ejercicio 3 - Suma solo la clave

def suma_clave(datos_2,clave_buscar):

    suma = 0

    for deporte, distancia in datos_2:
        if deporte == clave_buscar:
            suma += distancia
        
    return suma




datos = [10, 40, 60, 90]
datos_2=[("bici", 100), ("run", 30), ("bici", 50)]


print(num_menores(datos,50))
print(sport(datos_2,'bici'))
print(suma_clave(datos_2, 'bici'))