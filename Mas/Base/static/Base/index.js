document.querySelector(".navbar-nav").addEventListener("click", (event)=>{
    if (event.target.matches("a"))    
    event.target.classList.toggle("active");
    
})