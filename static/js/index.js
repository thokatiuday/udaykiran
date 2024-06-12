var header = document.getElementById('header');
var img = document.getElementById("profilepic")
var nav = document.getElementById('nav');
nav.style.marginTop = '230px';
img.style.height = '120px';
img.style.width = '120px';
header.style.height = '200px';

function scrool() {
    if (window.scrollY > 1) {
        header.style.height = '170px';
        img.style.height = '100px';
        img.style.width = '100px';
        nav.style.marginTop = '250px';
    } else {
        header.style.height = '200px';
        img.style.height = '120px';
        img.style.width = '120px';
        nav.style.marginTop = '230px';
    }
}

window.addEventListener('scroll', scrool);