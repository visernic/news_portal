/**
 * Main JavaScript File
 * Handles UI interactions and dynamic behaviors.
 */

"use strict";

document.addEventListener('DOMContentLoaded', function() {
    console.log('Visernic News Portal: Engine Started');

    // Auto-dismiss flash messages after 3 seconds
    const alerts = document.querySelectorAll('.alert-message');
    if (alerts.length > 0) {
        setTimeout(function() {
            alerts.forEach(function(alert) {
                alert.classList.add('fade-out');
                setTimeout(() => alert.remove(), 500);
            });
        }, 3000);
    }
    
    // Mobile Menu Toggle (Functionality placeholder)
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }
});
