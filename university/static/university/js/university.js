var univ_box

window.onload = function() {
    univ_box = document.getElementById('univ_box');
}


function univModel(){
    var shade_box = document.querySelector('#shade_box');
    var univ_box = document.querySelector('#univ-box');
    if (shade_box && univ_box)
    {
        console.log(shade_box);
        console.log(univ_box);
        univ_box.classList.add('active');
        shade_box.classList.add('active');
    }
}

function univModelExit(){
    var shade_box = document.querySelector('#shade_box');
    var univ_box = document.querySelector('#univ-box');
    shade_box.classList = 'shade-box';
    univ_box.classList = 'my-3 mx-5 university__form__box';
}