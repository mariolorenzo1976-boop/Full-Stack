// Crea 2 variables y muestra el Mayor de edad.

let nombre = "Mario";
let edad = 49;

if (edad>=18){
    console.log(edad);
}


// crear una función de saludar.

function saludar(){
    console.log("Hola Mario");
}

saludar();


// crea array y visualiza primero y último

let deportes = ["mtb", "running", "fuerza"];

console.log(deportes[0]);
console.log(deportes[deportes.length -1]);



// recorre array y calcula la suma total

let km = [10, 20, 30, 40];
let suma = 0;

for (let und of km){
    suma = suma + und
}
console.log(suma);


// Crea un objeto y muestralo

let bici = {
            modelo: "Turbo Levo",
            tipo: "MTB"
}


console.log(bici.modelo);
console.log(bici.tipo);


// Muestra solo los mayores de edad

let usuarios = [
    {nombre: "Mario", edad: 49},
    {nombre: "Ana", edad: 30},
    {nombre: "Pedro", edad: 17}
];

for(let mayor of usuarios){
    if (mayor.edad >= 18){
        console.log(mayor.nombre);
    }
}


// Cambia texto en pantalla al pulsar el botón 

let saludo = document.querySelector(".saludar");
let button = document.querySelector("button");

button.addEventListener("click", function(){
    saludo.textContent = "JavaScript funciona"
    

})


// Crea un contador

let counter = document.querySelector(".contador")
let button2 = document.querySelector(".contador-button")

let resultado = 0
button2.addEventListener("click", function(){
    resultado ++ 
    counter.textContent = resultado
})

// Saludar un hola nombre input al pulsar botón

nombreEntrada = document.querySelector(".nombre")
buttonSaludar = document.querySelector(".click-nombre")

buttonSaludar.addEventListener("click", function(){
    saludo.textContent = "Hola " + nombreEntrada.value
})


// crear un Login y Login con data base

let nameLogin = document.querySelector(".user")
let passwordLogin = document.querySelector(".password")
let confirmacionLogin = document.querySelector(".confirmacion")
let form = document.querySelector(".formulario")
let users = [
    { user: "Mario", pass: "123" },
    { user: "Ana", pass: "456" },
    { user: "Pedro", pass: "789" }
];


form.addEventListener("submit", function(event){
    event.preventDefault()
    let encontrado = false
    if (nameLogin.value == "" || passwordLogin.value == ""){
        confirmacionLogin.textContent = "Rellena los campos obligatoriamente"
        confirmacionLogin.style.color="red"
     
    }
    else 
    {
        for (let id of users){
            if (id.user == nameLogin.value && id.pass == passwordLogin.value){
                confirmacionLogin.textContent = "Login Correcto"
                confirmacionLogin.style.color="green"
                encontrado = true
                break;

            } 
            
        }

        if (encontrado == false){
           confirmacionLogin.textContent = "Usuario o Contraseña incorrectos";
           confirmacionLogin.style.color = "red";
        }

    }
         

})




