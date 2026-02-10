// Smooth Scrolling für Navigation Links - Event Delegation (nachhaltig optimiert)
document.addEventListener('click', function(e) {
    const anchor = e.target.closest('a[href^="#"]');
    if (anchor) {
        e.preventDefault();
        const target = document.querySelector(anchor.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }
});

// Header Scroll Effekt
let lastScroll = 0;
const header = document.querySelector('header');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    } else {
        header.style.boxShadow = 'none';
    }
    
    lastScroll = currentScroll;
});

// Portfolio Item Animationen beim Scrollen
const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            
            // Overlay-Animation nur auf Mobile (max-width 768px)
            if (window.innerWidth <= 768) {
                // Entferne alte Animation falls vorhanden
                entry.target.classList.remove('animate-overlay');
                
                // Trigger Animation nach kleiner Verzögerung
                setTimeout(() => {
                    entry.target.classList.add('animate-overlay');
                }, 300);
                
                // Entferne Klasse nach Animation (3 Sekunden)
                setTimeout(() => {
                    entry.target.classList.remove('animate-overlay');
                }, 3300);
            }
        }
    });
}, observerOptions);

document.querySelectorAll('.portfolio-item').forEach(item => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(30px)';
    item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(item);
});

// Video Autoplay beim Scrollen ins Viewport (nur wenn gewünscht)
// Videos starten nicht automatisch - Nutzer muss auf Play klicken
const videoObserverOptions = {
    threshold: 0.5
};

const videoObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        const video = entry.target;
        // Autoplay deaktiviert für bessere Barrierefreiheit
        // Nutzer entscheidet selbst, wann Video startet
        if (entry.isIntersecting) {
            // video.play(); // Deaktiviert
        } else {
            video.pause();
        }
    });
}, videoObserverOptions);

document.querySelectorAll('.project-video video').forEach(video => {
    videoObserver.observe(video);
});

// Slideshow Funktionalität
let currentSlide = 0;
let slides;
const dotsContainer = document.querySelector('.slide-dots');
let isMobile = window.innerWidth <= 768;

// Wähle die richtigen Slides basierend auf der Ansicht und entferne die anderen
if (isMobile) {
    // Entferne Desktop-Slides komplett aus dem DOM
    document.querySelectorAll('.slide.desktop-slide').forEach(slide => slide.remove());
    slides = document.querySelectorAll('.slide.mobile-slide');
} else {
    // Entferne Mobile-Slides komplett aus dem DOM
    document.querySelectorAll('.slide.mobile-slide').forEach(slide => slide.remove());
    slides = document.querySelectorAll('.slide.desktop-slide');
}

console.log('Found ' + slides.length + ' slides');

if (slides.length > 0) {
    // Erstelle Dots für jede Slide
    slides.forEach((_, index) => {
        const dot = document.createElement('span');
        dot.classList.add('dot');
        dot.setAttribute('role', 'button');
        dot.setAttribute('aria-label', `Zu Bild ${index + 1} wechseln`);
        dot.setAttribute('tabindex', '0');
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dot.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                goToSlide(index);
            }
        });
        dotsContainer.appendChild(dot);
    });

    const dots = document.querySelectorAll('.dot');

    function showSlide(n) {
        // Alle Slides verstecken
        slides.forEach(slide => slide.classList.remove('active'));
        
        // Alle dots deaktivieren
        dots.forEach(dot => {
            dot.classList.remove('active');
            dot.setAttribute('aria-pressed', 'false');
        });
        
        // Aktuellen Slide berechnen
        currentSlide = (n + slides.length) % slides.length;
        
        // Aktuellen Slide anzeigen
        slides[currentSlide].classList.add('active');
        
        // Aktuellen Dot aktivieren
        if (dots[currentSlide]) {
            dots[currentSlide].classList.add('active');
            dots[currentSlide].setAttribute('aria-pressed', 'true');
        }
        
        console.log('Showing slide ' + (currentSlide + 1) + ' of ' + slides.length);
    }

    function nextSlide() {
        showSlide(currentSlide + 1);
    }

    function prevSlide() {
        showSlide(currentSlide - 1);
    }

    function goToSlide(n) {
        showSlide(n);
    }

    // Event listeners
    document.querySelector('.slide-prev')?.addEventListener('click', prevSlide);
    document.querySelector('.slide-next')?.addEventListener('click', nextSlide);

    // Keyboard navigation for slideshow
    document.addEventListener('keydown', function(e) {
        if (slides.length > 0) {
            if (e.key === 'ArrowLeft') {
                prevSlide();
            } else if (e.key === 'ArrowRight') {
                nextSlide();
            }
        }
    });

    // Show first slide
    showSlide(0);
}

// Lightbox für Plakate
const lightbox = document.getElementById('posterLightbox');
const lightboxImg = document.getElementById('lightboxImage');
const lightboxDesc = document.getElementById('lightboxDescription');
const lightboxClose = document.querySelector('.lightbox-close');

if (lightbox) {
    // Event Delegation für alle Plakat-Bilder (nachhaltig optimiert - 1 statt N Listener)
    document.addEventListener('click', function(e) {
        const img = e.target.closest('.slide img');
        if (img) {
            lightboxImg.src = img.src;
            lightboxImg.alt = img.alt;
            lightboxDesc.textContent = img.getAttribute('data-description') || '';
            lightbox.classList.add('active');
            lightbox.setAttribute('aria-hidden', 'false');
            document.body.style.overflow = 'hidden';
            
            setTimeout(() => {
                lightboxClose.focus();
            }, 100);
        }
    });
    
    // Keyboard support für Bilder mit Event Delegation
    document.querySelectorAll('.slide img').forEach(img => {
        img.setAttribute('tabindex', '0');
        img.setAttribute('role', 'button');
        img.setAttribute('aria-label', `${img.alt} - Klicken zum Vergrößern`);
    });
    
    document.addEventListener('keydown', function(e) {
        const img = e.target.closest('.slide img');
        if (img && (e.key === 'Enter' || e.key === ' ')) {
            e.preventDefault();
            img.click();
        }
    });

    // Lightbox schließen
    function closeLightbox() {
        lightbox.classList.remove('active');
        lightbox.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = ''; // Scrolling wieder aktivieren
    }

    lightboxClose?.addEventListener('click', closeLightbox);
    
    // Klick außerhalb des Bildes schließt die Lightbox
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    // ESC-Taste schließt die Lightbox
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });
    
    // Initial aria-hidden setzen
    lightbox.setAttribute('aria-hidden', 'true');
}

// Email Popup
const emailLink = document.getElementById('emailLink');
const emailLinkAbout = document.querySelector('.email-link-about');
const emailPopup = document.getElementById('emailPopup');
const emailPopupClose = document.querySelector('.email-popup-close');

if (emailPopup) {
    // Funktion zum Öffnen des Popups
    function openEmailPopup(e) {
        e.preventDefault();
        emailPopup.classList.add('active');
        emailPopup.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        
        // Focus auf Close-Button setzen
        setTimeout(() => {
            emailPopupClose.focus();
        }, 100);
    }

    // Email-Link im Footer
    if (emailLink) {
        emailLink.addEventListener('click', openEmailPopup);
    }

    // Email-Link im About-Kontakt-Abschnitt
    if (emailLinkAbout) {
        emailLinkAbout.addEventListener('click', openEmailPopup);
    }

    // Close-Button Handler
    emailPopupClose?.addEventListener('click', function() {
        closeEmailPopup();
    });

    // Klick außerhalb schließt Popup
    emailPopup.addEventListener('click', function(e) {
        if (e.target === emailPopup) {
            closeEmailPopup();
        }
    });

    // ESC-Taste schließt Popup
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && emailPopup.classList.contains('active')) {
            closeEmailPopup();
        }
    });

    function closeEmailPopup() {
        emailPopup.classList.remove('active');
        emailPopup.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }

    // Initial aria-hidden setzen
    emailPopup.setAttribute('aria-hidden', 'true');
}

// Hero Video langsamer abspielen (0.5x Geschwindigkeit)
const heroVideo = document.querySelector('.project-hero video');
if (heroVideo) {
    heroVideo.playbackRate = 0.5;
}

console.log('Portfolio Website geladen - Emma Wagner');
