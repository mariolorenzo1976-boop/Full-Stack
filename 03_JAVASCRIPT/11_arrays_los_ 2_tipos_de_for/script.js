//ejercici 1 Muestra todos los valores usando for of

let deportes = ["MTB", "Running", "Natación"];

for (let deporte of deportes){
    console.log(deporte);
}


//ejercici 2 suma los valores y muestralos 

let kms = [10, 20, 30, 40];
let suma = 0;


for (km of kms){
    suma += km
}
console.log(suma);


//ejercici 3 muestra todas las edades >18

let edades = [12, 18, 25, 16, 30];

for (let edad of edades){
    if (edad >= 18){
        console.log(edad);
    }
}


//ejercici 4 encuentra actividad "running"

let actividades = ["MTB", "Running", "Fuerza"];

for (let actividad of actividades){
    if (actividad == "Running"){
        console.log("actividad: " + actividad + ", encontrada.")
    }
}


//ejercici 5 usa for clásico para recorrer el array

let bicis = ["Turbo-Levo", "Procaliber", "Gravel"];

for (let i=0; i < bicis.length; i++){
    console.log(bicis[i]);
}
