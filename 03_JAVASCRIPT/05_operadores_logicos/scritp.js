// operadores lógicos && Y, ! NO, || O.

// ejercicio comprueba si tienes casco y batería para salir en bici.

let bateria = 90;
let casco = true;

if (casco == true && bateria > 20) {
    console.log("puedes salir");
}


// ejercicio si llueve o hay viento , no sales

let llueve = true;
let viento = false;

if (llueve == true || viento == true) {
    console.log("No puedes salir");
} 


// ejercicio No conectado

let conectado = false;

if (conectado == false) {
    console.log("no hay conección")
}


// formas modernas

// if (casco == true)     --->.   if (casco)
// if (conectado == false). ->.   if (!conectado)

//EJERCICIO REPETIDOS CON FORMA MODERNA:
// // ejercicio comprueba si tienes casco y batería para salir en bici.
        let bateria2 = 90;
        let casco2 = true;

        if (casco2 && bateria2 > 20) {
            console.log("puedes salir");
        }

      // ejercicio si llueve o hay viento , no sales  

        let llueve2 = true;
        let viento2 = false;

        if (llueve2 || viento2) {
            console.log("No puedes salir");
        } 

        // ejercicio No conectado

        let conectado2 = false;

        if (!conectado2) {
            console.log("no hay conección")
        }



