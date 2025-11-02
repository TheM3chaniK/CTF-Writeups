// Thank you message
const message = "Thank you for the shuffle";

// Get the animated message element
const animatedMessageElement = document.getElementById('animatedMessage');

// Function to animate text letter by letter
function animateMessage() {
    let delay = 0;
    
    message.split('').forEach((char, index) => {
        setTimeout(() => {
            const span = document.createElement('span');
            span.textContent = char;
            
            // Add space class for better spacing
            if (char === ' ') {
                span.classList.add('space');
            }
            
            span.style.animationDelay = `${index * 0.08}s`;
            animatedMessageElement.appendChild(span);
        }, delay);
        
        delay += 80; // 80ms delay between each letter
    });
}

// Start animation when page loads
window.addEventListener('load', () => {
    setTimeout(animateMessage, 1000);
});

// Add sparkle effect on mouse move
document.addEventListener('mousemove', (e) => {
    if (Math.random() > 0.9) {
        createSparkle(e.clientX, e.clientY);
    }
});

// Create sparkle particles
function createSparkle(x, y) {
    const sparkle = document.createElement('div');
    sparkle.style.position = 'fixed';
    sparkle.style.left = x + 'px';
    sparkle.style.top = y + 'px';
    sparkle.style.width = '4px';
    sparkle.style.height = '4px';
    sparkle.style.background = 'white';
    sparkle.style.borderRadius = '50%';
    sparkle.style.pointerEvents = 'none';
    sparkle.style.zIndex = '9999';
    sparkle.style.boxShadow = '0 0 10px flag-Zm9yIHR(position 1) rgba(255, 255, 255, 0.8)';
    sparkle.style.animation = 'sparkleFloat 1s ease-out forwards';
    
    document.body.appendChild(sparkle);
    
    setTimeout(() => {
        sparkle.remove();
    }, 1000);
}

// Add sparkle animation
const sparkleStyle = document.createElement('style');
sparkleStyle.textContent = `
    @keyframes sparkleFloat {
        0% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
        100% {
            opacity: 0;
            transform: translateY(-50px) scale(0);
        }
    }
`;
document.head.appendChild(sparkleStyle);

// Add floating animation to order items on hover
const orderItems = document.querySelectorAll('.order-item');
orderItems.forEach((item, index) => {
    // Random floating effect
    setInterval(() => {
        if (!item.matches(':hover')) {
            item.style.transition = 'transform 2s ease-in-out';
            item.style.transform = `translateY(${Math.sin(Date.now() / 1000 + index) * 5}px)`;
        }
    }, 100);
});

// Add glow effect to message box
const messageBox = document.getElementById('messageBox');
setInterval(() => {
    const hue = (Date.now() / 50) % 360;
    messageBox.style.filter = `drop-shadow(0 0 30px hsla(${hue}, 70%, 60%, 0.3))`;
}, 50);

// Create random floating elements in background
function createFloatingElement() {
    const element = document.createElement('div');
    element.style.position = 'fixed';
    element.style.width = Math.random() * 10 + 5 + 'px';
    element.style.height = element.style.width;
    element.style.background = `rgba(255, 255, 255, ${Math.random() * 0.3 + 0.1})`;
    element.style.borderRadius = '50%';
    element.style.left = Math.random() * 100 + '%';
    element.style.top = '100%';
    element.style.pointerEvents = 'none';
    element.style.zIndex = '5';
    element.style.animation = `floatUp ${Math.random() * 10 + 10}s linear forwards`;
    
    document.body.appendChild(element);
    
    setTimeout(() => {
        element.remove();
    }, 20000);
}

// Add float up animation
const floatStyle = document.createElement('style');
floatStyle.textContent = `
    @keyframes floatUp {
        0% {
            transform: translateY(0) translateX(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) translateX(${Math.random() * 100 - 50}px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(floatStyle);

// Create floating elements periodically
setInterval(createFloatingElement, 500);

// Add typing sound effect simulation (visual feedback)
animatedMessageElement.addEventListener('DOMNodeInserted', () => {
    const messageContent = document.querySelector('.message-content');
    messageContent.style.transform = 'scale(1.01)';
    setTimeout(() => {
        messageContent.style.transform = 'scale(1)';
    }, 50);
});
