// ejercicio 8 Cambia el texto al pulsar botón

let titulo = document.querySelector(".titulo");

let boton = document.querySelector("button");

boton.addEventListener("click", function(){
    titulo.textContent = "JavaScript funciona"
})

// Ejercicio 9 Cambia atrbutos color azul fondo amarillo al pulsar botón

let title = document.querySelector(".titulo");
let button = document.querySelector(".buttonColor");

button.addEventListener("click", function(){
    title.style.color = "blue"
    title.style.backgroundColor = "yellow"

})



