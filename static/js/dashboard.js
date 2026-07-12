/* ==========================================
   TransitOps Dashboard Interaction Logic
   ========================================== */

document.addEventListener("DOMContentLoaded", function () {
    // Automatically close django notifications/messages alerts after 5 seconds
    const alerts = document.querySelectorAll(".alert-dismissible");
    alerts.forEach(function (alert) {
        setTimeout(function () {
            // Check if bootstrap alert is present and dismiss it
            if (typeof bootstrap !== 'undefined' && bootstrap.Alert) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            } else {
                alert.style.transition = "opacity 0.5s ease";
                alert.style.opacity = "0";
                setTimeout(() => alert.remove(), 500);
            }
        }, 5000);
    });

    // Handle mobile sidebar toggle behavior
    const sidebarToggle = document.querySelector('[data-bs-target="#sidebarMenu"]');
    const sidebarMenu = document.getElementById("sidebarMenu");

    if (sidebarToggle && sidebarMenu) {
        sidebarToggle.addEventListener("click", function () {
            sidebarMenu.classList.toggle("show");
        });
    }
});
