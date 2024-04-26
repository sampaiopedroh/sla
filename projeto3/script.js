let imagens=['./img/Carro1.jpg','./img/Carro2.jpg','./img/Carrro3.jpg'];
let index=0;
let time=3000;


function slideShow(){

    document.getElementById("imgbanner").src=imagens[index];
    index++;

    if(index == imagens.length){
        index=0;
    }
    setTimeout('slideShow()',time)
}
slideShow();

const btnMobile = document.querySelector('#btnMob');
function menu(){
    const navBar = document.querySelector('#nav');
    navBar.classList.toggle('active');
}

btnMobile.addEventListener('click', menu);