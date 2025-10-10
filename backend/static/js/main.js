const swiper = new Swiper('.slider_swiper', {
  loop: true,
  slidesPerView: 'auto',
  centeredSlides: true,
  spaceBetween: 30,

  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },

  // 🔹 Avtomatik aylanish
  autoplay: {
    delay: 5000, // 3 soniyada almashadi
    disableOnInteraction: false, // foydalanuvchi bosganda ham davom etadi
  },
});


const swiper2 = new Swiper("#sliderbox", {
  slidesPerView: 1.5,
  spaceBetween: 20,
  loop: true,
  navigation: {
    nextEl: '.swiper-button-nextid',
    prevEl: '.swiper-button-previd',
  },
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  breakpoints: {
    1200: { slidesPerView: 4 },
    768: { slidesPerView: 2.5 },
    500: { slidesPerView: 1.5 },
  }
});

var swiper3 = new Swiper("#sliderbox2", {
  slidesPerView: 1.5,
  spaceBetween: 20,
  loop: true,
  navigation: {
    nextEl: '.swiper-button-nextid2',
    prevEl: '.swiper-button-previd2',
  },
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  breakpoints: {
    1200: { slidesPerView: 5 },
    768: { slidesPerView: 2.5 },
    500: { slidesPerView: 1.5 },
  }
});


// 1-qator (o‘ngga yuradi)
const swiper4 = new Swiper("#logosrow1", {
  slidesPerView: 2,
  spaceBetween: 20,
  loop: true,
  navigation: {
    nextEl: '#swiper-button-next2',
    prevEl: '#swiper-button-prev2',
  },
  autoplay: {
    delay: 0,                // uzluksiz harakat
    disableOnInteraction: false,
  },
  speed: 3000,               // tezligi (silliq yurishi uchun)
  breakpoints: {
    1200: { slidesPerView: 5 },
    768: { slidesPerView: 3 },
    500: { slidesPerView: 2 },
  },
  mousewheel: true,          // scroll bilan boshqarish
});

// 2-qator (chapga yuradi)
var swiper5 = new Swiper("#logosrow2", {
  slidesPerView: 2,
  spaceBetween: 20,
  loop: true,
  navigation: {
    nextEl: '#swiper-button-next2',
    prevEl: '#swiper-button-prev2',
  },
  autoplay: {
    delay: 0,
    disableOnInteraction: false,
    reverseDirection: true,  // chapga yuradi
  },
  speed: 3000,
  breakpoints: {
    1200: { slidesPerView: 5 },
    768: { slidesPerView: 3 },
    500: { slidesPerView: 2 },
  },
  mousewheel: true,
});
// Accordion toggle
document.querySelectorAll(".acardion-header").forEach(header => {
    header.addEventListener("click", () => {
        let content = header.nextElementSibling;
        content.classList.toggle("active");
        header.classList.toggle("active");
    });
});

document.addEventListener("DOMContentLoaded", () => {
  const headers = document.querySelectorAll(".acardion_header");

  headers.forEach(header => {
    header.addEventListener("click", function () {
      const content = this.nextElementSibling;
      const item = this.parentElement;

      if (item.classList.contains("open")) {
        // yopish
        content.style.height = content.scrollHeight + "px"; 
        requestAnimationFrame(() => {
          content.style.height = "0";
        });
        item.classList.remove("open");
      } else {
        // ochish
        item.classList.add("open");
        content.style.height = content.scrollHeight + "px";

        // animatsiya tugagach auto qilish (moslashuvchan bo‘lishi uchun)
        content.addEventListener("transitionend", () => {
          if (item.classList.contains("open")) {
            content.style.height = "auto";
          }
        }, { once: true });
      }
    });
  });
});
 let activebt = document.querySelectorAll('#catmenuid_desctop .menu-item-has-children > a');

activebt.forEach(function(item) {
  item.addEventListener('click', function(e) {
    e.preventDefault();

    // аввало, ҳамма очиқ менюларни ёпиб чиқамиз
    activebt.forEach(function(other) {
      if (other !== item) {
        other.parentElement.classList.remove('showopen');
      }
    });

    // кейин эса шу босилганини toggle қиламиз
    this.parentElement.classList.toggle('showopen');
  });
});
 
const thumbs = new Swiper(".gallery-thumbs", {
  direction: "horizontal", // Desktop uchun
  spaceBetween: 10,
  slidesPerView: 2.5,
  freeMode: true,
  watchSlidesProgress: true,
  watchSlidesVisibility: true,
  loop: true,

  breakpoints: {
    // 950px dan kichik bo‘lsa (planshet va mobil)
    950: {
      direction: "vertical",
      slidesPerView: 4,
    },
    768: {
      direction: "horizontal",
      slidesPerView: 4,
    },
    480: {
      direction: "horizontal",
      slidesPerView: 3,
    },
     380: {
      direction: "horizontal",
      slidesPerView: 3,
    }
  }
});

const main = new Swiper(".gallery-top", {
  spaceBetween: 10,
  loop: true,
  thumbs: {
    swiper: thumbs,
  },
});

menuController('line1id','closedesktopid','catmenuid_desctop');
let slideMenu = document.querySelectorAll('#slideMenu_menuid .menu-item-has-children > a');
let backButtons = document.querySelectorAll('#slideMenu_menuid .sub_menu li:first-child a'); // faqat "Назад"

slideMenu.forEach(function(item) {
  item.addEventListener('click', function(e) {
    e.preventDefault();

    // Boshqa ochilganlarni yopamiz
    slideMenu.forEach(function(other) {
      if (other !== item) {
        other.parentElement.classList.remove('openshow');
      }
    });

    // Shu item'ni ochamiz
    item.parentElement.classList.toggle('openshow');
  });
});

// "Назад" tugmasiga ishlov
backButtons.forEach(function(back) {
  back.addEventListener('click', function(e) {
    e.preventDefault();

    // "Назад" tugmasi joylashgan .sub_menu → .menu-item-has-children'ni yopamiz
    let parentMenu = back.closest('.menu-item-has-children');
    parentMenu.classList.remove('openshow');
  });
});




// Price Range
const minRange = document.getElementById("minRange");
const maxRange = document.getElementById("maxRange");
const minPrice = document.getElementById("minPrice");
const maxPrice = document.getElementById("maxPrice");
const rangeTrack = document.querySelector(".range-track");
if (minRange && maxRange && minPrice && maxPrice && rangeTrack){
function updateRange() {
    let minVal = parseInt(minRange.value);
    let maxVal = parseInt(maxRange.value);

    if (minVal > maxVal - 10000) { // minimal farq
        minRange.value = maxVal - 10000;
        minVal = maxVal - 10000;
    }

    minPrice.textContent = minVal.toLocaleString();
    maxPrice.textContent = maxVal.toLocaleString();

    let percent1 = (minVal / minRange.max) * 100;
    let percent2 = (maxVal / maxRange.max) * 100;

    rangeTrack.style.left = percent1 + "%";
    rangeTrack.style.width = (percent2 - percent1) + "%";
}

minRange.addEventListener("input", updateRange);
maxRange.addEventListener("input", updateRange);

}


function toggleFavorite(el){
    const productId = el.dataset.productId;

    fetch(`/favorite/toggle/${productId}/`, {method: 'POST', headers:{
        'X-CSRFToken': '{{ csrf_token }}'
    }})
    .then(response => response.json())
    .then(data => {
        if(data.favorited){
            el.classList.remove('fa-regular');
            el.classList.add('fa-solid', 'text-danger'); // qizil heart
        } else {
            el.classList.remove('fa-solid', 'text-danger');
            el.classList.add('fa-regular');
        }
    });
}



// main.js

 function menuController(activeid, removeid, showbutton) {
    const line1id = document.getElementById(activeid);
    const removeBtn = document.getElementById(removeid);
    const catmenuid = document.getElementById(showbutton);

    if (line1id && removeBtn && catmenuid) {
        line1id.addEventListener('click', function () {
            catmenuid.classList.add("activemenu");
        });

        removeBtn.addEventListener('click', function () {
            catmenuid.classList.remove("activemenu");
        });
    } else {
        console.warn("menuController elementlaridan biri topilmadi:", activeid, removeid, showbutton);
    }
}



const overlays = document.querySelectorAll(".video-overlay");
  const ytVideo = document.getElementById("ytVideo");

  overlays.forEach(overlay => {
    overlay.addEventListener("click", () => {
      const videoId = overlay.dataset.video;
      overlays.forEach(o => o.style.display = "none"); // Boshqa overlay’larni ham yashirish
      ytVideo.style.display = "block";
      ytVideo.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&mute=1`;
    });
  });
  

 
function toggleFavorite(event, el) {
    event.preventDefault();
    let productId = el.getAttribute("data-id");

    fetch(`/store/wishlist/toggle/${productId}/`, {
        method: "GET",
        headers: { "X-Requested-With": "XMLHttpRequest" }
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "added") {
            // Yurakni qizil qilish
            el.querySelector("path").setAttribute("stroke", "red");
        } else if (data.status === "removed") {
            // Yurakni kulrang qilish
            el.querySelector("path").setAttribute("stroke", "#A6A6A6");
        }

        // Headerdagi counterni yangilash
        let counter = document.querySelector(".wishlist span");
        if (counter) {
            counter.textContent = data.count;
        }
    })
    .catch(err => console.error(err));
}

function toggleFavorite(el) {
    let productId = el.getAttribute("data-product-id");

    fetch(`/store/wishlist/toggle/${productId}/`, {
        method: "GET",
        headers: {"X-Requested-With": "XMLHttpRequest"}
    })
    .then(res => res.json())
    .then(data => {
        // Yurak rangini o'zgartirish
        if(data.status === "added") {
            el.classList.remove("fa-regular");
            el.classList.add("fa-solid");
        } else {
            el.classList.remove("fa-solid");
            el.classList.add("fa-regular");
        }

        // Header countni yangilash
        let wishlistCountEl = document.getElementById("wishlist-count");
        if(wishlistCountEl) {
            wishlistCountEl.innerText = data.count;
        }
    })
    .catch(err => console.log(err));
}

