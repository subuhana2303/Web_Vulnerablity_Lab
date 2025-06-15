// Web Vulnerability Lab - Client-side JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize syntax highlighting
    if (typeof Prism !== 'undefined') {
        Prism.highlightAll();
    }

    // Add copy functionality to code blocks
    addCopyButtons();

    // Form validation enhancements
    enhanceFormValidation();

    // Add warning confirmations for vulnerable actions
    addVulnerabilityWarnings();

    // Auto-dismiss alerts after 5 seconds
    autoDismissAlerts();
});

function addCopyButtons() {
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach(function(codeBlock) {
        const pre = codeBlock.parentNode;
        const button = document.createElement('button');
        
        button.className = 'btn btn-sm btn-outline-secondary position-absolute top-0 end-0 m-2';
        button.innerHTML = '<i class="fas fa-copy"></i>';
        button.title = 'Copy code';
        
        pre.style.position = 'relative';
        pre.appendChild(button);
        
        button.addEventListener('click', function() {
            navigator.clipboard.writeText(codeBlock.textContent).then(function() {
                button.innerHTML = '<i class="fas fa-check text-success"></i>';
                setTimeout(function() {
                    button.innerHTML = '<i class="fas fa-copy"></i>';
                }, 2000);
            });
        });
    });
}

function enhanceFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            // Add loading state to submit buttons
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<span class="loading me-2"></span>Processing...';
                submitBtn.disabled = true;
                
                // Re-enable button after 3 seconds (in case of errors)
                setTimeout(function() {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    });
}

function addVulnerabilityWarnings() {
    // Add warnings for vulnerable form submissions
    const vulnerableForms = document.querySelectorAll('form[action*="vulnerable"]');
    
    vulnerableForms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            const confirmed = confirm(
                '⚠️ You are about to submit to a VULNERABLE endpoint!\n\n' +
                'This is for educational purposes only. In a real application, ' +
                'this could be exploited by attackers.\n\n' +
                'Continue with the demonstration?'
            );
            
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
}

function autoDismissAlerts() {
    const alerts = document.querySelectorAll('.alert-dismissible');
    
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
}

// Utility function to highlight potentially dangerous input
function highlightDangerousInput(input) {
    const dangerousPatterns = [
        /<script/i,
        /javascript:/i,
        /on\w+=/i,
        /union\s+select/i,
        /or\s+1=1/i,
        /drop\s+table/i
    ];
    
    const value = input.value;
    const isDangerous = dangerousPatterns.some(pattern => pattern.test(value));
    
    if (isDangerous) {
        input.classList.add('border-warning');
        
        // Add warning tooltip
        if (!input.dataset.bsToggle) {
            input.setAttribute('data-bs-toggle', 'tooltip');
            input.setAttribute('data-bs-placement', 'top');
            input.setAttribute('title', 'This input contains potentially dangerous content');
            new bootstrap.Tooltip(input);
        }
    } else {
        input.classList.remove('border-warning');
    }
}

// Add input monitoring for educational purposes
document.addEventListener('input', function(event) {
    if (event.target.tagName === 'INPUT' || event.target.tagName === 'TEXTAREA') {
        highlightDangerousInput(event.target);
    }
});

// Add demonstration helpers
window.VulnLab = {
    // Insert example payloads
    insertPayload: function(inputId, payload) {
        const input = document.getElementById(inputId);
        if (input) {
            input.value = payload;
            input.focus();
            highlightDangerousInput(input);
        }
    },
    
    // Show security tip
    showSecurityTip: function(message) {
        const toast = document.createElement('div');
        toast.className = 'toast align-items-center text-white bg-info border-0 position-fixed top-0 end-0 m-3';
        toast.style.zIndex = '9999';
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    <i class="fas fa-lightbulb me-2"></i>${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;
        
        document.body.appendChild(toast);
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
        
        toast.addEventListener('hidden.bs.toast', function() {
            document.body.removeChild(toast);
        });
    }
};

// Add keyboard shortcuts for quick payload insertion
document.addEventListener('keydown', function(event) {
    // Ctrl+Shift+1: SQL Injection payload
    if (event.ctrlKey && event.shiftKey && event.key === '!') {
        const sqlInput = document.querySelector('input[name="username"]');
        if (sqlInput) {
            VulnLab.insertPayload(sqlInput.id, "' OR '1'='1");
            event.preventDefault();
        }
    }
    
    // Ctrl+Shift+2: XSS payload
    if (event.ctrlKey && event.shiftKey && event.key === '@') {
        const xssInput = document.querySelector('textarea[name="content"]');
        if (xssInput) {
            VulnLab.insertPayload(xssInput.id, "<script>alert('XSS')</script>");
            event.preventDefault();
        }
    }
});

console.log('🛡️ Web Vulnerability Lab loaded successfully!');
console.log('Educational shortcuts:');
console.log('  Ctrl+Shift+1: Insert SQL injection payload');
console.log('  Ctrl+Shift+2: Insert XSS payload');
