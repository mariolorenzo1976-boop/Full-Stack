usuario = {"nombre": "Emilia", "apellido": "García", "edad": 30, "ciudad": "Madrid", "peso": 83}

# imprimimos las claves del diccionario usuario utilizando un bucle for, que recorre cada clave del diccionario y la imprime. En este caso, las claves son "nombre", "apellido", "edad" y "ciudad".
for clave in usuario:
    print(clave)


# imprimimos la clave - valor del diccionario
for clave, valor in usuario.items():
    print(clave,valor)


# imprimimos solo el valor
for valor in usuario.values():
    print(valor)



# miramos si la clave edad existe en el diccionario, utilizamos un for
variable = 0
for clave in usuario:
    if clave == "edad":
        variable = 1

if variable == 1:   
    print(f"La clave: {clave} existe")
else:   
    print("la clave edad no existe ")


# miramos si la clave edad existe en el diccionario, sin for
clave = "edad"
if clave in usuario:
    print(f"la clave: {clave} existe")
else:
    print(f"la calve: {clave} no existe ")


# miramos que el valor 83 está dentro del diccionario
valor = 83
if valor in usuario.values():
    print("el valor 83 existe")
else:
    print("el valor 83 no existe")

