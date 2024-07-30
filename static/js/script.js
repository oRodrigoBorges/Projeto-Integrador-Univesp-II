document.addEventListener('DOMContentLoaded', function() {
    var menuIcon = document.querySelector('.iconeMenu');
    var menuLateral = document.getElementById('menuLateral');
    var sobreposição = document.getElementById('sobreposição');
    var fecharMenu = document.getElementById('fecharMenu');

    menuIcon.addEventListener('click', function() {
        menuLateral.classList.add('active');
        sobreposição.classList.add('active');
    });

    fecharMenu.addEventListener('click', function() {
        menuLateral.classList.remove('active');
        sobreposição.classList.remove('active');
    });

    sobreposição.addEventListener('click', function() {
        menuLateral.classList.remove('active');
        sobreposição.classList.remove('active');
    });
});
