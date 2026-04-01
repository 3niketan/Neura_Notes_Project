let moonIcon = document.getElementById("moonIcon");
let sunIcon = document.getElementById("sunIcon");
let body = document.body;

// Dark mode
moonIcon.addEventListener("click", function () {
    body.classList.remove("light-mode");
    body.classList.add("dark-mode");

    moonIcon.classList.add("d-none");
    sunIcon.classList.remove("d-none");
});

// Light mode
sunIcon.addEventListener("click", function () {
    body.classList.remove("dark-mode");
    body.classList.add("light-mode");

    sunIcon.classList.add("d-none");
    moonIcon.classList.remove("d-none");
});