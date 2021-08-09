let quesPoint;
let inputPoint;
let innerPoint;
let questionDetail;

window.onload = function () {
    quesPoint = document.querySelector("#ques_point");
    inputPoint = document.querySelector("#question__input__point");
    innerPoint = document.querySelector("#ques_point");

    questionDetail = document.getElementById("post-area");
    var questionArticle = document.getElementsByClassName("question__article");
    console.log(questionDetail);
    console.log(questionArticle[0]);

    if(questionDetail){
        console.log(questionArticle[0]);
        questionArticle[0].classList.remove('active');
    }



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
