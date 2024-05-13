var swiper = new Swiper(".popular-conten", {
    slidesPerView: 1,
    spaceBetween: 10,
    autoplay:{
        delay:755500,
        disableOnInteraction:false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints:{
    280:{
    slidesPerView: 1,
    spaceBetween: 10,},
    300:{
    slidesPerView: 2,
    spaceBetween: 10,},
    540:{
    slidesPerView: 2,
    spaceBetween: 10,},
    758:{
    slidesPerView: 3,
    spaceBetween: 15,},
    900:{
    slidesPerView: 4,
    spaceBetween: 20,},
}
});