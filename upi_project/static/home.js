var openpopupBtn = document.querySelector("#open-popup-btn");
var closePopBtn = document.querySelector(".popup-close-btn");

openpopupBtn.addEventListener("click", function(){
    document.body.classList.add("popup-active")
});

closePopBtn.addEventListener("click",function(){
    document.body.classList.remove("popup-active")
});