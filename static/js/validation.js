// Client-side validation for OWASP compliance
document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('register-form');
    
    if (registerForm) {
        registerForm.addEventListener('submit', function(e) {
            const password1 = document.getElementById('id_password1');
            const password2 = document.getElementById('id_password2');
            
            // OWASP password requirements
            if (password1.value.length < 12) {
                alert('Password must be at least 12 characters long (OWASP requirement)');
                e.preventDefault();
                return false;
            }
            
            if (password1.value !== password2.value) {
                alert('Passwords do not match');
                e.preventDefault();
                return false;
            }
            
            // Check for common passwords
            const commonPasswords = [
                'password', '123456', 'qwerty', 'admin', 'welcome',
                'password123', '123456789', '12345678', '12345'
            ];
            
            if (commonPasswords.includes(password1.value.toLowerCase())) {
                alert('Password is too common. Please choose a stronger password.');
                e.preventDefault();
                return false;
            }
        });
    }
    
    // Add security info tooltips
    const securityIcons = document.querySelectorAll('.security-icon');
    securityIcons.forEach(icon => {
        icon.addEventListener('mouseover', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'security-tooltip';
            tooltip.textContent = this.dataset.tooltip || 'Security feature implemented';
            tooltip.style.position = 'absolute';
            tooltip.style.background = '#333';
            tooltip.style.color = 'white';
            tooltip.style.padding = '5px';
            tooltip.style.borderRadius = '3px';
            tooltip.style.zIndex = '1000';
            this.appendChild(tooltip);
        });
        
        icon.addEventListener('mouseout', function() {
            const tooltip = this.querySelector('.security-tooltip');
            if (tooltip) {
                tooltip.remove();
            }
        });
    });
});