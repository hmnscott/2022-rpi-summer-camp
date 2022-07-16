function toggleDIV() {
    var x = document.getElementById("toggle-me");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function toggleDIVbgcolor() {
    var x = document.getElementById("toggle-me");
    x.classList.toggle("dark-mode");
}