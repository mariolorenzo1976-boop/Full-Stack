document.querySelectorAll('.texto-completo').forEach(bloque => {

    let hideText_btn = bloque.querySelector('.readMore_btn');
    let hideText = bloque.querySelector('.hideText');

    hideText_btn.addEventListener('click', () => {

        hideText.classList.toggle('show');

        if(hideText.classList.contains('show')){
            hideText_btn.innerHTML = 'Leer menos...';
        }
        else{
            hideText_btn.innerHTML = 'Leer más...';
        }

    });

});