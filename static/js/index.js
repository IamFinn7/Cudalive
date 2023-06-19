var element = document.getElementsByClassName("create_room")[0];

document.getElementById("create").addEventListener("click", function () {
    element.style.display = "flex";
});

document.getElementById("close").addEventListener("click", function () {
    element.style.display = "none";
});
