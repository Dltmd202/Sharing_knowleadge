
window.addEventListener("DOMContentLoaded", (e) => {
    e.preventDefault();
    showPassword();
})

function showPassword() {
    var inputs = document.getElementsByClassName("password-input");
    document.getElementById("show-password-btn").addEventListener("click", (e) => {
        e.preventDefault();
        for (var i = 0; i < inputs.length; ++i) {
            if (inputs[i].type === "password") {
                inputs[i].type = "text";
            } else {
                inputs[i].type = "password";
            }
        }
        
    });
}

