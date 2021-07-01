
window.addEventListener("DOMContentLoaded", (e) => {
    e.preventDefault();
    showPassword();
})

function showPassword() {
    var input = document.getElementById("password-input");
    document.getElementById("show-password-btn").addEventListener("click", (e) => {
        e.preventDefault();
        if (input.type === "password") {
            input.type = "text";
        } else {
            input.type = "password";
        }
    });
}

