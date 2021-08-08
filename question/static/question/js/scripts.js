let quesPoint;
let inputPoint;
let innerPoint

window.onload = function () {
    quesPoint = document.querySelector("#ques_point");
    inputPoint = document.querySelector("#question__input__point");
    innerPoint = document.querySelector("#ques_point").innerText;
    console.log(document.querySelector("#question__input__point"));
    console.log(inputPoint.innerText);
    document.querySelector("#question__input__point").addEventListener('keyup',
        function(event){
            console.log(event);
            console.log(inputPoint.value);
            console.log(innerPoint);
            console.log(inputPoint.value + innerPoint);
            if (parseInt(inputPoint.value) > parseInt(innerPoint)){
                alert("질문 포인트가 부족합니다.");
                inputPoint.value = parseInt(innerPoint);
            }
        }
        )
}
