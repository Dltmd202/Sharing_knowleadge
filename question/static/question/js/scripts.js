let quesPoint;
let inputPoint;
let innerPoint;
let questionDetail;
let commentButton;

window.onload = function () {
    quesPoint = document.querySelector("#ques_point");
    inputPoint = document.querySelector("#question__input__point");
    innerPoint = document.querySelector("#ques_point");
    commentButton = document.getElementById("comment_button");

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

// 신고 모달 내용 변경 기능
function reportClassClicked(pk, back=false) {
    const reportClassList = document.getElementsByClassName("reportClassLists");
    for (var i = 0; i < reportClassList.length; ++i) {
        reportClassList[i].hidden = !back;
    }
    document.getElementsByClassName("reportClassLink")[pk-1].hidden = back;
}

// 신고 내용 전달 기능
function convertReportText(pk) {
    const reportText = document.getElementById("reportText-" + pk).innerHTML;
    document.getElementById("reportTextArea").value = reportText;
    document.getElementById("reportClassInput").value = pk
    const form = document.getElementById("reportForm");
    form.submit();
}

// 질문 or 답변 신고인지 표시해주는 기능
function checkReportType(type, pk) {
    document.getElementById("reportTypeInput").value = type;
    document.getElementById("reportPKInput").value = pk

}
  
function commentButtonActive(id){
    console.log("comment_area_" + id);
    console.log(document.getElementById("comment_area_" + id));
    document.getElementById("comment_area_" + id ).classList.toggle('active');
}