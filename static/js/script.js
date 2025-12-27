const homepage = window.location.pathname === '/';
const navbar = document.querySelector('.navbar');

if (homepage){
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