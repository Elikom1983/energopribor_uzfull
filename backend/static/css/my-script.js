// AOS.init();

const getImages = document.querySelectorAll('.project-item-sub-box img'),
      setImage = document.querySelector('.project-item-block img');
     
getImages.forEach((item) => {
  item.addEventListener("click", (e) => {
    const itemSrc = item.getAttribute("src");
    console.log(itemSrc);
    if(e.target === item) {
      setImage.setAttribute("src", itemSrc);
    }
  })
});

const fs = document.querySelectorAll('.for_change');

function changeFs(){
  fs.forEach(txt => {
    if (txt.innerHTML.length > 25) {
      txt.style.fontSize = '50px';
    }
  });
 
}
changeFs();