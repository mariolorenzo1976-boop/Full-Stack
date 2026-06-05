// Ejercicio 1 objetos básicos

let bici = {"modelo": "turbo-levo",
            "tipo": "eMTB",
            "ruedas": 29
            }


console.log(bici.modelo);
console.log(bici.tipo);
console.log(bici.ruedas);


// Ejercicio 2 modificar objeto

let persona = {"nombre": "Mario",
                "edad": 49
}

persona.edad = "50";
persona.ciudad =  "La Laguna";

console.log(persona);


// Ejercicio 3 objeto con array muestra el primer deporte y el último

let usuario = {"nombre": "Ana",
               "deporte": ["MTB","Running","Fuerza"] 
}

console.log(usuario.deporte[0]);
console.log(usuario.deporte[usuario.deporte.length -1])
