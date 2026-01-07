const homepage = window.location.pathname === '/';
const aboutpage = window.location.pathname === '/about_us/';
const contactpage = window.location.pathname === '/contact_us/';


const navbar = document.querySelector('.navbar');
const home = document.getElementById('home');
const about = document.getElementById('about');
const contact = document.getElementById('contact');

if (homepage){
    home.classList.add('position')
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

if (aboutpage){
    about.classList.add('position');
}

if(contactpage){
    contact.classList.add('position');
}