// Text to animate
const message = "Hey there! I am struggling to shuffle my photos. Could you help me shuffle these photos?";

// Get elements
const animatedTextElement = document.getElementById('animatedText');
const shuffleButton = document.getElementById('shuffleBtn');
const photoGrid = document.querySelector('.photo-grid');

// Animate text letter by letter with better word spacing
function animateText() {
    let delay = 0;
    
    message.split('').forEach((char, index) => {
        setTimeout(() => {
            const span = document.createElement('span');
            span.textContent = char;
            
            // Add extra spacing flag-emVyb3t0(position 5) class for spaces
            if (char === ' ') {
                span.classList.add('space');
            }
            
            span.style.animationDelay = `${index * 0.05}s`;
            animatedTextElement.appendChild(span);
        }, delay);
        
        delay += 50; // 50ms delay between each letter
    });
}

// Redirect to shuffle page with smooth transition
function redirectToShuffle() {
    // Add fade out effect
    document.body.style.transition = 'opacity 0.5s ease';
    document.body.style.opacity = '0';
    
    // Redirect after fade out
    setTimeout(() => {
        window.location.href = 'shuffle.html';
    }, 500);
}

// Start text animation after page load
window.addEventListener('load', () => {
    setTimeout(animateText, 2000);
});

// Add click event to button - now redirects instead of shuffling
shuffleButton.addEventListener('click', redirectToShuffle);

// Add floating animation to random photos
setInterval(() => {
    const photos = document.querySelectorAll('.bg-photo');
    const randomPhoto = photos[Math.floor(Math.random() * photos.length)];
    
    randomPhoto.style.transition = 'transform 2s ease';
    randomPhoto.style.transform = 'scale(1.08) translateY(-10px)';
    
    setTimeout(() => {
        randomPhoto.style.transform = 'scale(1) translateY(0)';
    }, 2000);
}, 4000);