let user = document.querySelector(".usuario");
let password = document.querySelector(".contraseña");
let confirm = document.querySelector(".confimación")
let form = document.querySelector(".formulario")

let usuarios = [
    { user: "Mario", pass: "123" },
    { user: "Ana", pass: "456" }
];

form.addEventListener("submit", function(event){
    event.preventDefault()
    
    let encontrado = false
    let validation = false
    
    if(user.value == "" || password.value == ""){
        confirm.textContent = "Rellene todos los campos antes de proceder"
        confirm.style.color="red"
        validation = false
    }
        else {
       
        validation = true

        
    }
    
    if (validation == true){
        for(let id of usuarios){
            if (id.user == user.value){
                encontrado = true
                confirm.textContent = "Este usuario ya existe"
                confirm.style.color="red"
                user.value=""
                password.value=""
                break;
            } 
        }       
    }
    
    if (encontrado == false && validation == true){
        usuarios.push({user:user.value, pass:password.value}) 
        console.log(usuarios)
        confirm.textContent = "usuario creado"
        confirm.style.color="green"
        user.value=""
        password.value=""       
    }
    
})


 