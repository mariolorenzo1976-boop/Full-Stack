let form = document.querySelector(".contact-form");
let name = document.querySelector(".input-name-form");
let email = document.querySelector(".input-email-form");
let text = document.querySelector(".input-text-form");
let confirm = document.querySelector(".confirmation")

let send = []

form.addEventListener("submit", function(event){
        event.preventDefault();  

        if (name.value == "" || email.value == "" || text.value ==""){
            console.log("Introduce datos");
            confirm.textContent="Introduce datos obligatorios";
            confirm.style.color= "red";
            return;
        }
        else
        {
            send.push({name:name.value, email:email.value, text: text.value});
            confirm.textContent="Mensaje enviado";
            confirm.style.color= "green";
            console.log(send);
            form.reset();
        }
})