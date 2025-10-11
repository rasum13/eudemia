const sidebar = document.querySelector('.sidebar');

let sidebar_shown = false;
function toggleSidebar() {
    if (sidebar_shown) {
        sidebar.classList.remove('show');
        sidebar_shown = false;
    }
    else {
        sidebar.classList.add('show');
        sidebar_shown = true;
    }
}