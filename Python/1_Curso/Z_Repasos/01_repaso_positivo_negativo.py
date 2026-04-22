numeros = []
dato = 1
positivo = 0
negativo = 0
while dato !=0:
     dato = int(input("Introduce números hasta 0:"))
     if dato < 0:
          numeros.append(dato)
          negativo +=1
     if dato > 0:
          numeros.append(dato)
          positivo +=1
     
print(f"los numeros números introducidos son: {numeros}, hay {negativo} números negativos y {positivo}, números positivos")
