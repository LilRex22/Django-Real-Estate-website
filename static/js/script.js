
const navbar = document.querySelector('.navbar');

const pages = {
    '/': document.getElementById('home'),
    '/about_us/': document.getElementById('about'),
    '/contact_us/': document.getElementById('contact'),
    '/explore/': document.getElementById('explore'),
};

const currentPage = window.location.pathname;  // this will return either one of the pages keys

if (pages[currentPage]) {   // pages['/' or 'about_us/' or 'contact_us/'] which is the value of the currentpage
    pages[currentPage].classList.add('position');
    window.addEventListener('scroll', ()=>{
        if (window.scrollY > 0){
            navbar.classList.add('nav_bg');
            navbar.classList.remove('nav_tp');
        }
        else{
            navbar.classList.remove('nav_bg');
            navbar.classList.add('nav_tp');
        }
    });
}