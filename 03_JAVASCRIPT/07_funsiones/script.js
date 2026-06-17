// ejercicio 1 crea una funsion y ejecutala 2 veces.

function bienvenida(nombre){
    console.log("bienvenido/a: " + nombre);

}

bienvenida("Mario");
bienvenida("Ana");
bienvenida("Pepe")


// ejercicio 2 crea una funsion que muestre tu deporte es MTB


function mostrarDeporte(deporte){
    console.log("Tu deporte es: " + deporte)
}


mostrarDeporte("MTB");
mostrarDeporte("Running");



// ejercicio 3 crea una funsion que reste

function resta(a, b){
    return a - b;
}

resultado = resta( 10, 5);
console.log(resultado);




// ejercicio 4 comprueba edad

function compruebaEdad(edad){
    if (edad >= 18){
        return "mayor de edad"
    }
    else{
        return "menor de edad"
    }
}

edad = compruebaEdad(5)
console.log(edad);

console.log(compruebaEdad(20))



