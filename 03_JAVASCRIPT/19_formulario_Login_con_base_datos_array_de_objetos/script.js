let usuario = document.querySelector(".usuario");
let password = document.querySelector(".password");
let mensaje = document.querySelector(".mensaje");
let form = document.querySelector(".formulario");

let usuarios = [
    { user: "Mario", pass: "123" },
    { user: "Ana", pass: "456" },
    { user: "Pedro", pass: "789" }
];
let encontrado = false  

form.addEventListener("submit", function(event){
    event.preventDefault()

    if (usuario.value == "" || password.value == ""){
        mensaje.textContent = "Rellene los campos"
        mensaje.style.color = "red"

    }
    else {

        for (let users of usuarios){
            
            if (users.user == usuario.value && users.pass == password.value){
                encontrado = true;
                break;
            }
            
        }
        
        }

        if (encontrado == true){
            mensaje.textContent = "Datos Correctos";
            mensaje.style.color = "green";
        }
        else{
            mensaje.textContent = "Usuario o Contraseña incorrectos";
            mensaje.style.color = "red";

        }
        encontrado = false
})
