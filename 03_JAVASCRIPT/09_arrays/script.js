// imprime el segundo elemento del array

let nombres = ["Mario", "Victor", "Juan"];

console.log(nombres[1]);

// añade Eva al array

nombres.push("Eva");

console.log(nombres);

// recorre el array

for (nombre of nombres){
    console.log(nombre);
}

// Guardar un elemento del array en una variable

let deportes = ["MTB", "runing", "swim"];

let deporte = deportes[1]

console.log(deporte)


// Modificar un elemento de un array

let sports = ["MTB", "runing", "swim"];

sports[1] = "trail-running"

console.log(sports);

// cuantos elementos tiene

console.log(sports.length);


// último elemento

console.log(sports[sports.length - 1])


// Array de boleanos

let estados = [true, false, true]

