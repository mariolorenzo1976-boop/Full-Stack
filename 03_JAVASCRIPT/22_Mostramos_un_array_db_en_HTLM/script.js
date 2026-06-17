let user = document.querySelector(".usuario");
let password = document.querySelector(".contraseña");
let confirm = document.querySelector(".confimación")
let form = document.querySelector(".formulario")

//CAPTURAMOS EL <ul> para crear la lista
let listta = document.querySelector(".lista-usuarios")

//CREAMOS EL ELEMENTO <li>


//METEMOS UN DATO EL <li>
// li.textContent = "Mario"

// // ESCRIBIMOS EL HTLM <li>
// listta.appendChild(li);

// BASE DATOS

let usuarios = [
    { user: "Mario", pass: "123" },
    { user: "Ana", pass: "456" }
];




// FUNCIÓN PARA CREAR BOTÓN

function crearBotonEliminar(){
    let button = document.createElement("Button")
        button.textContent = "Eliminar"
        listta.appendChild(button)

}




// FUNSIÓN PARA MOSTRAR LA LISTA

function mostrarLista(){
    listta.innerHTML = ""; //Limpia la lista

    for (let usuario of usuarios){
        let li = document.createElement("li");
        li.textContent =usuario.user;
        crearBotonEliminar(li);
        listta.appendChild(li);


}}

// MOSTRAR LISTA AL CARGAR

mostrarLista()

// EVENTO FORMULARIO

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
        mostrarLista()
        user.value=""
        password.value="" 
        user.focus() 
        
            
    }
    
})


 