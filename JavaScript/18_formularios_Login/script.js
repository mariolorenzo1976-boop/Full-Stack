let usuario = document.querySelector(".usuario");
let password = document.querySelector(".password");
let mensaje = document.querySelector(".mensaje");
let form = document.querySelector(".formulario"); 


form.addEventListener("submit", function(event){
    event.preventDefault();

    if (usuario.value == "" || password.value == ""){
        mensaje.textContent = "Rellena los campos";
    }
    else if(usuario.value == "Mario" && password.value == "123"){
        mensaje.textContent = "Login Correcto";
        mensaje.style.color = "Green";
    }
    else {
        mensaje.textContent = "Login Incorrecto";
        mensaje.style.color = "red";
    }

    


});