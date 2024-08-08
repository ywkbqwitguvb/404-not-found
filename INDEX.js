document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.getElementById('nav-links');
    
    menuToggle.addEventListener('click', function () {
        navLinks.classList.toggle('active');
    });

    // Set active link based on current URL
    const navItems = document.querySelectorAll('nav ul li a');
    navItems.forEach(item => {
        if (item.href === window.location.href) {
            item.classList.add('active');
        }
    });
});
