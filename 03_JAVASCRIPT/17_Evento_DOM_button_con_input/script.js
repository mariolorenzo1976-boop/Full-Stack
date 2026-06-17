let nombreInput = document.querySelector(".nombre");
let SaludarButton = document.querySelector(".saludar");
let mensajeH2 = document.querySelector(".mensaje");

SaludarButton.addEventListener("click", function(){
    mensajeH2.textContent = "Hola " + nombreInput.value;
    
})
