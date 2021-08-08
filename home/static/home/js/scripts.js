
var input_box;
var input_box_height;

window.onload = function () {
    input_box = document.getElementById('input-box');
    header = document.querySelector('header');
    var questionForm = document.querySelector(".question__form");
    var questionArticle = document.getElementsByClassName("question__article");
    if (questionForm) {
        console.log("questionForm " + questionForm);
        console.log("questionArticle " + questionArticle[0]);
        questionArticle[0].classList.remove('active');
    }
}

window.addEventListener('scroll', function(){
    var header = document.querySelector('header');
    let scrollLocation = document.documentElement.scrollTop;
    var toggledNav = document.querySelector("header .active");
    if (toggledNav === null){
        header.classList.toggle('sticky', window.scrollY > 0);
    }
	// let windowHeight = window.innerHeight;
	// let fullHeight = document.body.scrollHeight;
    // console.log(input_box.scrollHeight, header.scrollHeight, scrollLocation)
	// if(scrollLocation >= input_box.scrollHeight + header.scrollHeight){
	// 	console.log('끝')
	// }
});

function toggleMenu(){
    var menuToggle = document.querySelector('.toggle');
    var menu = document.querySelector('.menu');
    menuToggle.classList.toggle('active')
    menu.classList.toggle('active')

}

function report(){
    alert("신고가 접수되었습니다")
}

var searchCategory = document.querySelector('#search__category__detail')

function searchBox(id){
    var boxes = document.getElementsByClassName('search__detail');
    var activated = document.getElementsByClassName('active');
    var searchClass = document.getElementsByClassName('search__class');
    if (activated[0]){
        console.log(activated[0].id)
        console.log(id)
    }

    if (activated[0] && activated[0].id === id){
        for(i = 0; i < boxes.length; i ++){
            boxes[i].classList = 'search__detail deactivate';
            searchClass[i].classList = 'search__class';
        }
    }
    else {
        for (i = 0; i < boxes.length; i++) {
            boxes[i].classList = 'search__detail'
            searchClass[i].classList = 'search__class';
            if (boxes[i].id === id) {
                boxes[i].classList.add('active');
                searchClass[i].classList.add('active__class');
            } else{
                boxes[i].classList.add('deactivate')
            }
        }
    }
}

const toggleBtn = document.querySelector(".nav__toggle");
const nav_utils = document.querySelector(".nav-utils");
const account = document.querySelector(".account");
var header = document.querySelector('header');

toggleBtn.addEventListener("click", ()=> {
    var toggledNav = document.getElementsByClassName("sticky");
    console.log(toggledNav[0]);
    console.log(nav_utils);
    nav_utils.classList.toggle('active');
    account.classList.toggle('active');
    if (toggledNav[0] === undefined){
        header.classList.toggle('sticky');
    } else{
        header.classList.toggle('sticky', window.scrollY > 0);
    }
});

var categoryBtn = document.querySelector("#category__toggle__button");
console.log(categoryBtn);
categoryBtn.addEventListener("click", ()=>{
    var categoryList = document.querySelector("#category__list");
    console.log(categoryList);
    categoryList.classList.toggle('active');
})


