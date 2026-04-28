datos = (100, 200, 300, 400, 500)

# Aquí imprimimos cada elemento de la tupla, pero sin modificar la tupla, ya que las tuplas son inmutables. Para ello, utilizamos un bucle for, que recorre cada elemento de la tupla,  y lo imprime. La variable n toma el valor de cada elemento de la tupla en cada iteración del bucle. Al final, imprimimos cada elemento de la tupla en una línea diferente.  
for n in datos:
    print(n)



# aquí sumamos cada elemento de la tupla, pero sin modificar la tupla, ya que las tuplas son inmutables. Para ello, utilizamos un bucle for, que recorre cada elemento de la tupla, y lo suma a una variable llamada suma, que se va actualizando en cada iteración del bucle. Al final, imprimimos el resultado de la suma de los elementos de la tupla.
suma = 0    
for n in datos:
    suma += n
print(suma) 


# aquí miramos si el número 200 está en la tupla, utilizando un bucle for, que recorre cada elemento de la tupla, y una estructura condicional if, que evalúa si el elemento n es igual a 200. Si es así, imprime "elemento encontrado", y si no es así, imprime "elemento no encontrado". Al final, imprimimos el resultado de la búsqueda del número 200 en la tupla. 
for n in datos:
   if n == 200:
       print("elemento encontrado")

   else:
         print("elemento no encontrado")