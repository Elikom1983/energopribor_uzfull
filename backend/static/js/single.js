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
