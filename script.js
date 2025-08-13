document.addEventListener('DOMContentLoaded', function() {
    // Get all audio elements
    const audioElements = document.querySelectorAll('audio');
    
    // Get control buttons
    const playAllBtn = document.getElementById('playAllBtn');
    const stopAllBtn = document.getElementById('stopAllBtn');
    const pauseAllBtn = document.getElementById('pauseAllBtn');
    
    // Play all audio files
    playAllBtn.addEventListener('click', function() {
        audioElements.forEach(audio => {
            audio.play().catch(error => {
                console.log('Audio playback failed:', error);
            });
        });
        
        // Visual feedback
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 150);
    });
    
    // Stop all audio files
    stopAllBtn.addEventListener('click', function() {
        audioElements.forEach(audio => {
            audio.pause();
            audio.currentTime = 0;
        });
        
        // Visual feedback
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 150);
    });
    
    // Pause all audio files
    pauseAllBtn.addEventListener('click', function() {
        audioElements.forEach(audio => {
            audio.pause();
        });
        
        // Visual feedback
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 150);
    });
    
    // Add individual audio controls
    audioElements.forEach((audio, index) => {
        // Add event listeners for individual audio controls
        audio.addEventListener('play', function() {
            console.log(`Audio ${index + 1} started playing`);
        });
        
        audio.addEventListener('pause', function() {
            console.log(`Audio ${index + 1} paused`);
        });
        
        audio.addEventListener('ended', function() {
            console.log(`Audio ${index + 1} finished playing`);
        });
        
        audio.addEventListener('error', function(e) {
            console.error(`Error with audio ${index + 1}:`, e);
        });
    });
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        switch(e.key.toLowerCase()) {
            case 'p':
                if (e.ctrlKey) {
                    e.preventDefault();
                    playAllBtn.click();
                }
                break;
            case 's':
                if (e.ctrlKey) {
                    e.preventDefault();
                    stopAllBtn.click();
                }
                break;
            case ' ':
                if (e.ctrlKey) {
                    e.preventDefault();
                    pauseAllBtn.click();
                }
                break;
        }
    });
    
    // Add tooltips for keyboard shortcuts
    playAllBtn.title = 'Play All (Ctrl+P)';
    stopAllBtn.title = 'Stop All (Ctrl+S)';
    pauseAllBtn.title = 'Pause All (Ctrl+Space)';
    
    // Add loading state for audio elements
    audioElements.forEach(audio => {
        audio.addEventListener('loadstart', function() {
            this.style.opacity = '0.7';
        });
        
        audio.addEventListener('canplay', function() {
            this.style.opacity = '1';
        });
        
        audio.addEventListener('error', function() {
            this.style.opacity = '0.5';
            this.style.border = '2px solid #f44336';
        });
    });
    
    // Add visual feedback for audio pairs
    const audioPairs = document.querySelectorAll('.audio-pair');
    audioPairs.forEach(pair => {
        const audios = pair.querySelectorAll('audio');
        
        // Check if any audio in the pair is playing
        function updatePairStatus() {
            const isPlaying = Array.from(audios).some(audio => !audio.paused);
            if (isPlaying) {
                pair.style.borderColor = '#4CAF50';
                pair.style.boxShadow = '0 15px 40px rgba(76, 175, 80, 0.3)';
            } else {
                pair.style.borderColor = 'transparent';
                pair.style.boxShadow = '0 10px 30px rgba(0,0,0,0.2)';
            }
        }
        
        audios.forEach(audio => {
            audio.addEventListener('play', updatePairStatus);
            audio.addEventListener('pause', updatePairStatus);
            audio.addEventListener('ended', updatePairStatus);
        });
    });
    
    // Add smooth scrolling for better UX
    const smoothScrollTo = (target) => {
        target.scrollIntoView({
            behavior: 'smooth',
            block: 'center'
        });
    };
    
    // Add click to scroll to audio pair functionality
    audioPairs.forEach(pair => {
        const title = pair.querySelector('h3');
        title.style.cursor = 'pointer';
        title.addEventListener('click', () => {
            smoothScrollTo(pair);
        });
        
        // Add hover effect for clickable title
        title.addEventListener('mouseenter', () => {
            title.style.color = '#5a6fd8';
        });
        
        title.addEventListener('mouseleave', () => {
            title.style.color = '#667eea';
        });
    });
    
    // Add search/filter functionality
    const searchBox = document.createElement('input');
    searchBox.type = 'text';
    searchBox.placeholder = 'Search audio pairs...';
    searchBox.className = 'search-box';
    searchBox.style.cssText = `
        width: 100%;
        max-width: 400px;
        padding: 12px 20px;
        margin: 0 auto 30px auto;
        display: block;
        border: 2px solid #ddd;
        border-radius: 25px;
        font-size: 16px;
        outline: none;
        transition: border-color 0.3s ease;
    `;
    
    searchBox.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        
        audioPairs.forEach(pair => {
            const title = pair.querySelector('h3').textContent.toLowerCase();
            if (title.includes(searchTerm)) {
                pair.style.display = 'block';
                pair.style.animation = 'fadeInUp 0.6s ease forwards';
            } else {
                pair.style.display = 'none';
            }
        });
    });
    
    // Insert search box after header
    const header = document.querySelector('header');
    header.parentNode.insertBefore(searchBox, header.nextSibling);
    
    // Add focus styles for search box
    searchBox.addEventListener('focus', function() {
        this.style.borderColor = '#667eea';
        this.style.boxShadow = '0 0 10px rgba(102, 126, 234, 0.3)';
    });
    
    searchBox.addEventListener('blur', function() {
        this.style.borderColor = '#ddd';
        this.style.boxShadow = 'none';
    });
    
    console.log('Audio Pairs Website loaded successfully!');
    console.log(`Total audio elements: ${audioElements.length}`);
    console.log(`Total audio pairs: ${audioPairs.length}`);
});
