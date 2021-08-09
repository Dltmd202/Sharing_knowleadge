
function searchQuestion() {
    let serachValue = document.getElementById('search-input').value.trim()
    if (serachValue.length > 1) {
        location.href = "question/search/" + serachValue +"/"
    } else {
        alert("검색어가 짧습니다");
    }
}

document.getElementById('search-input').addEventListener('keyup',
    function (event){
    if(event.key === 'Enter'){
        searchQuestion()
    }
});

function navSearchQuestion() {
    let serachValue = document.getElementById('nav-search-input').value.trim()
    if (serachValue.length > 1) {
        location.href = "question/search/" + serachValue +"/"
    } else {
        alert("검색어가 짧습니다");
    }
}
document.getElementById('nav-search-input').addEventListener('keyup',
    function (event){
    if(event.key === 'Enter'){
        searchQuestion()
    }
    });


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