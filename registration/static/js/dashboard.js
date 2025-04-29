document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('darkModeToggle');
    const body = document.body;
    const toggleText = document.querySelector('#darkModeToggle .toggle-text');
    const moonIcon = document.querySelector('#darkModeToggle .bi-moon-stars-fill');

    // Check if dark mode is already enabled
    if (localStorage.getItem('darkMode') === 'enabled') {
        body.classList.add('dark-mode');
        toggleText.textContent = 'Light Mode';
        moonIcon.classList.remove('bi-moon-stars-fill');
        moonIcon.classList.add('bi-sun-fill');
    }

    toggleButton.addEventListener('click', () => {
        body.classList.toggle('dark-mode');

        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
            toggleText.textContent = 'Light Mode';
            moonIcon.classList.remove('bi-moon-stars-fill');
            moonIcon.classList.add('bi-sun-fill');
        } else {
            localStorage.setItem('darkMode', 'disabled');
            toggleText.textContent = 'Dark Mode';
            moonIcon.classList.remove('bi-sun-fill');
            moonIcon.classList.add('bi-moon-stars-fill');
        }
    });
});