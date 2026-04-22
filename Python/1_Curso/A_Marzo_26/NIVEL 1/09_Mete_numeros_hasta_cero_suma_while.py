numero=1
contador=0
suma=0
signo_negativo=0
signo_positivo=0
while numero != 0:
        numero = int(input ("Introduce un número, el 0 finaliza :"))
        if numero >0:
            signo_positivo +=1
            contador += 1
            suma = suma + numero
        elif numero <0:
            signo_negativo +=1
            contador += 1
            suma = suma + numero
        else:
             numero=0
      
        
if contador!=0:
    print(f"Has introducido {contador} y eso suman {suma} y una media de {suma/contador}, y haz metido {signo_positivo} números positivos y {signo_negativo} números negativos")
else:
     print("Te has salido sin introducir ningún número")