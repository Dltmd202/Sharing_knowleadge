
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
