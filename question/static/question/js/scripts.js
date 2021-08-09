let quesPoint;
let inputPoint;
let innerPoint;
let questionDetail;
let questionArticle;

window.onload = function () {
    quesPoint = document.querySelector("#ques_point");
    inputPoint = document.querySelector("#question__input__point");
    innerPoint = document.querySelector("#ques_point");

    questionDetail = document.getElementsByClassName("question__form");
    questionArticle = document.getElementsByClassName("question__article");
    console.log(questionDetail[0]);
    console.log(questionArticle[0]);

    
    console.log(document.querySelector("#question__input__point"));

    if(inputPoint){
        inputPoint.addEventListener('keyup',
            function(event){
                console.log(event);
                console.log(inputPoint.value);
                console.log(innerPoint.innerText);
                console.log(inputPoint.value + innerPoint);
                if (parseInt(inputPoint.value) > parseInt(innerPoint.innerText)){
                    alert("질문 포인트가 부족합니다.");
                    inputPoint.value = parseInt(innerPoint.innerText);
                }
            }
        );
    }
}
