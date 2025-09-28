$(document).ready(function () {
  const plusImg = document.querySelector(".image-box figure"),
    addImg = document.querySelector(".img_section");
  const images = document.querySelectorAll("img");

  if (plusImg) {
    plusImg.addEventListener("click", () => {
      addImg.classList.add("img_section_active");
    });
  }

  if (addImg !== null) {
    addImg.addEventListener("click", () => {
      addImg.classList.remove("img_section_active");
    });
  }

  if (images) {
    images.forEach((item) => item.setAttribute("loading", "lazy"));
  }
  // const inp = document.querySelectorAll(input);
  // inp.setAttribute('')
  // SLIDER
  // const newGoods = document.querySelector(".new__goods"),
  //   newGoodsOwl = newGoods.querySelector(".owl-stage"),
  //   newGoodsOwlNext = newGoods.querySelector(".owl-nav .owl-next");
  // newGoodsOwl.style.transistion = "all 110s linear";

  // setInterval(() => {
  //   console.log(1);
  //   newGoodsOwlNext.click();
  // }, 900);
});
// $(".class1").marquee({
//   speed: 50,
//   gap: 0,
//   delayBeforeStart: 0,
//   duplicated: true,
//   pauseOnHover:true,
//   startVisible:true
// })


const fs = document.querySelectorAll('.for_change');

function changeFs(){
  fs.forEach(txt => {
    if (txt.innerHTML.length > 25) {
      txt.style.fontSize = '25px';
    }
  });
 
}
changeFs();



const getAtr = document.querySelectorAll('.onClick_about'),
      setAtr = document.querySelector('.for__img_details img'),
      changeClassBlock = document.querySelector('.img_section_about');

function changeImgAbout() {
  getAtr.forEach((item) => {
    item.addEventListener('click', (e) =>{
      const newSrc = e.getAttribute('src');
    })

  })
  setAtr.setAttribute('src', newSrc);
  changeClassBlock.classList.add('img_section_active');
  
}
changeImgAbout();
