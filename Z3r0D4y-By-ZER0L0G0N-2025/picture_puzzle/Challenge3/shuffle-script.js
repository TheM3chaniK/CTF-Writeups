// Get all shuffle buttons
const shuffleButtons = document.querySelectorAll('.shuffle-btn');
const popup = document.getElementById('popupMessage');
const popupText = document.querySelector('.popup-text');
const popupClose = document.querySelector('.popup-close');
const nextPageBtn = document.getElementById('nextPageBtn');
const prevPageBtn = document.getElementById('prevPageBtn');

// Messages for each photo based on position
const messages = {
    1: "Make it 3rd picture",
    2: "Make it 5th picture",
    3: "Make it 6th picture",
    4: "Make it 2nd picture",
    5: "Make it 1st picture",
    6: "Make it 4th picture"
};

// Add click event to each shuffle button
shuffleButtons.forEach((button) => {
    button.addEventListener('click', (e) => {
        e.stopPropagation();
        
        const photoBox = button.closest('.photo-box');
        const position = photoBox.getAttribute('data-position');
        
        // Show popup with appropriate message
        showPopup(messages[position]);
        
        // Add special animation to the clicked box
        photoBox.style.transform = 'scale(0.95)';
        setTimeout(() => {
            photoBox.style.transform = '';
        }, 200);
    });
});

// Function to show popup
function showPopup(message) {
    popupText.textContent = message;
    popup.classList.add('active');
    
    // Add celebration effect
    createConfetti();
}

// Close popup
popupClose.addEventListener('click', () => {
    popup.classList.remove('active');
});

// Close popup when clicking outside
popup.addEventListener('click', (e) => {
    if (e.target === popup) {
        popup.classList.remove('active');
    }
});

// Next Page Button - Redirect with fade effect
nextPageBtn.addEventListener('click', () => {
    document.body.style.transition = 'opacity 0.5s ease';
    document.body.style.opacity = '0';
    
    setTimeout(() => {
        window.location.href = 'next-page.html';
    }, 500);
});

// Previous Page Button - Redirect to index.html with fade effect
prevPageBtn.addEventListener('click', () => {
    document.body.style.transition = 'opacity 0.5s ease';
    document.body.style.opacity = '0';
    
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 500);
});

// Create confetti effect
function createConfetti() {
    const colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe', '#43e97b'];
    const confettiCount = 50;
    
    for (let i = 0; i < confettiCount; i++) {
        setTimeout(() => {
            const confetti = document.createElement('div');
            confetti.style.position = 'fixed';
            confetti.style.width = '10px';
            confetti.style.height = '10px';
            confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            confetti.style.left = Math.random() * 100 + '%';
            confetti.style.top = '-10px';
            confetti.style.borderRadius = '50%';
            confetti.style.zIndex = '9999';
            confetti.style.pointerEvents = 'none';
            confetti.style.animation = `fall ${Math.random() * 3 + 2}s linear forwards`;
            
            document.body.appendChild(confetti);
            
            setTimeout(() => {
                confetti.remove();
            }, 5000);
        }, i * 30);
    }
}

// Add confetti animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fall {
        to {
            transform: translateY(100vh) rotate(360deg);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Add floating animation variation on hover
const photoBoxes = document.querySelectorAll('.photo-box');
photoBoxes.forEach((box, index) => {
    box.addEventListener('mouseenter', () => {
        box.style.transition = 'transform 0.3s ease';
    });
    
    box.addEventListener('mouseleave', () => {
        box.style.transition = 'transform 0.3s ease';
    });
});

// Add ripple effect on click
photoBoxes.forEach(box => {
    box.addEventListener('click', function(e) {
        // Only create ripple if not clicking the button
        if (e.target.classList.contains('shuffle-btn')) {
            return;
        }
        
        const ripple = document.createElement('div');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.style.position = 'absolute';
        ripple.style.borderRadius = '50%';
        ripple.style.background = 'rgba(255, 255, 255, 0.5)';
        ripple.style.transform = 'scale(0)';
        ripple.style.animation = 'ripple 0.6s ease-out';
        ripple.style.pointerEvents = 'none';
        
        this.querySelector('.photo-wrapper').appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

// Add ripple animation
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    .photo-wrapper {
        position: relative;
        overflow: hidden;
    }
`;
document.head.appendChild(rippleStyle);

// Add keyboard support (ESC to close popup)
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && popup.classList.contains('active')) {
        popup.classList.remove('active');
    }
});

// Add sparkle effect on hover
photoBoxes.forEach(box => {
    box.addEventListener('mouseenter', function() {
        createSparkles(this);
    });
});

function createSparkles(element) {
    const sparkleCount = 5;
    const rect = element.getBoundingClientRect();
    
    for (let i = 0; i < sparkleCount; i++) {
        setTimeout(() => {
            const sparkle = document.createElement('div');
            sparkle.innerHTML = '✨';
            sparkle.style.position = 'fixed';
            sparkle.style.left = (rect.left + Math.random() * rect.width) + 'px';
            sparkle.style.top = (rect.top + Math.random() * rect.height) + 'px';
            sparkle.style.fontSize = '20px';
            sparkle.style.zIndex = '9999';
            sparkle.style.pointerEvents = 'none';
            sparkle.style.animation = 'sparkle 1s ease-out forwards';
            
            document.body.appendChild(sparkle);
            
            setTimeout(() => {
                sparkle.remove();
            }, 1000);
        }, i * 100);
    }
}

// Add sparkle animation
const sparkleStyle = document.createElement('style');
sparkleStyle.textContent = `
    @keyframes sparkle {
        0% {
            opacity: 1;
            transform: scale(0) rotate(0deg);
        }
        50% {
            opacity: 1;
            transform: scale(1) rotate(180deg);
        }
        100% {
            opacity: 0;
            transform: scale(0) rotate(360deg);
        }
    }
`;
document.head.appendChild(sparkleStyle);