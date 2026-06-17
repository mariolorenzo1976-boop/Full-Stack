//ejercicio 1 muestra la primera, la segunda y tercera bici

let bikes = ["turbo-levo", "procaliber", "gravel"]

for (bike of bikes){
    console.log(bike)
}

console.log(bikes[0]);
console.log(bikes[1]);
console.log(bikes[2]);



//ejercicio 2 añade Natación

let deportes = ["MTB", "Runnig"]

deportes.push("Natación")
console.log(deportes);


//ejercicio 3 muestra el primer y último valor

let kms = [20, 35, 50, 80]

console.log(kms[0]);
console.log(kms [kms.length -1]);


//ejercicio 4 cambia running por trail-running

let actividades = ["mtb", "running", "fuerza"];
let contador = 0;

for (actividad of actividades){
    if (actividad == "running"){
        actividades[contador]="trail-running"
       
    }
     contador = contador + 1
}
console.log(actividades);