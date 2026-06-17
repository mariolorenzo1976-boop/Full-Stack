// crea las siguientes variables y muestralas en consola

let nombre = "Mario";
let edad= 49;
let ciudad = "La Laguna";

console.log("nombre: " + nombre + " edad: " + edad + " ciudad: " + ciudad);

console.log(nombre);
console.log(edad);
console.log(ciudad);



// suma y muestra resultado

let precio = 120;
let descuento = 25;

console.log(precio - descuento);


// suma y muestra resultado

console.log("hola: " + nombre + " tienes: " + edad + " años ");


//if simple, si es menor qu 20 carga bici

let batería = 25;

if (batería < 20){
    console.log("carga la bici")
    }
    else {
    console.log("bici lista para la ruta")

    }


//9 o más -> Sobresaliente
// 5 o más -> Aprobado
// menos de 5 -> Suspendido

let nota = 969;

if (nota < 5){
    console.log("suspendido");

}
else if (nota > 4 && nota < 9){
    console.log("aprobado");

}
else if (nota > 8 && nota <= 10){
    console.log("sobresaliente");
}
else if (nota < 0 || nota >10){
    console.log(" nota incorrecta")
}


//si tiene casco y la batería es mayor que 20

let casco = true;
let bateria = 70;

if (casco = true && bateria > 20){
    console.log("Ruta iniciada");
}

//si llueve o hace viento quedate en casa

let lluvia = false;
let viento = true;

if (lluvia == true || viento == true){
    console.log("entrena en casa")

}


//fución sencilla


function saludar(nombre){
    console.log("Hola " + nombre);
}

saludar("Ana");
saludar("Emma");



//fución sencilla varios parámetros


function presentar(nombre, edad){
    console.log(nombre + " tiene " + edad + " años")
}

presentar("mario" , 25);


//fución sencilla que retorna valor 

function suma(a, b){
    return a + b;
}

let resultado = suma(2222, 5)
console.log(resultado)


