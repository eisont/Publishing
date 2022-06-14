var nextBtn = document.querySelector(".next_btn");
var prevBtn = document.querySelector(".prev_btn");
var sliderSection = document.querySelector(".slider_section")

nextBtn.addEventListener("click", function () {
    sliderSection.style.background = "url(../images/chanel/1932.jpg) center center no-repeat";

    sliderSection.style.backgroundSize = "contain";
});

prevBtn.addEventListener("click", function () {
    sliderSection.style.background = "";
})



var logo = document.querySelector(".header > .logo");
var logoA = document.querySelector(".header > .logo > a");

function changeColorBlue() {
    logo.style.background = "blue";
};

function changeColorOrigin() {
    logo.style.background = "";
}

logo.addEventListener("mouseover", function (){
    changeColorBlue();
});

logoA.addEventListener("mouseover", function(){
    logoA.style.padding = "19px 0";
})
logo.addEventListener("mouseout", changeColorOrigin);
logoA.addEventListener("mouseout", function(){
    logoA.style.padding= "";
})

var textHover = document.querySelector(".nav > .gnb > li > a:first-child");
var textHover_2 = document.querySelectorAll(".nav > .gnb > li > a")[1];
var textHover_3 = document.querySelectorAll(".nav > .gnb > li > a")[2];


textHover.addEventListener("click", function(){
    prompt("prompt 함수 사용.");
});
textHover_2.addEventListener("click", function(){
    alert("alert 함수 사용")
})
textHover_3.addEventListener("click", function (){
    document.write("document.write()함수 사용")
})





var gallery_01 = document.querySelector(".gallery_list > li:first-child > a > figure > img");
var gallery_02 = document.querySelector(".gallery_list > li:last-child > a > figure > img");


gallery_01.addEventListener("mouseover", function(){
    gallery_01.setAttribute("src", "../images/chanel/1957.jpg")    
});

gallery_01.addEventListener("mouseout", function(){
    gallery_01.setAttribute("src", "images/p_images/gallery_01.jpg")    
});


gallery_02.addEventListener("mouseover", function(){
    gallery_02.setAttribute("src", "../images/chanel/BEIGE.jpg")        
});
gallery_02.addEventListener("mouseout", function(){
    gallery_02.setAttribute("src", "images/p_images/gallery_02.jpg")        
});