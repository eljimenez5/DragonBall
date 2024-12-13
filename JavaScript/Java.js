const btnUp = document.getElementById('btn-up');

btnUp.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});