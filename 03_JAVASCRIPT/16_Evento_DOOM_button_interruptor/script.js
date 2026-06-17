// Ejercicio interruptor + contador
let titulo = document.querySelector(".titulo");
let boton = document.querySelector(".interruptor");
let contador = document.querySelector(".contador");

let activo = true;


let counter = 0;
boton.addEventListener("click", function(){
    if (activo){
        titulo.textContent = "Hola Mundo";
        activo = false;
        
    }
    else{
        titulo.textContent = "Hola Mario";
        activo = true;
        
    }
    counter ++;
    contador.textContent = counter;
    
})