var univ_box

window.onload = function() {
    univ_box = document.getElementById('univ_box');
}


function compModel(){
    var shade_box = document.querySelector('#company_shade_box');
    var company_box = document.querySelector('#company-box');
    if (shade_box && company_box)
    {
        console.log(shade_box);
        console.log(univ_box);
        company_box.classList.add('active');
        shade_box.classList.add('active');
    }
}

function companyModelExit(){
    var shade_box = document.querySelector('#company_shade_box');
    var company_box = document.querySelector('#company-box');
    shade_box.classList = 'shade-box';
    company_box.classList = 'my-3 mx-5 company__form__box';
}