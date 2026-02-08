// Service Worker für nachhaltiges Caching
// Reduziert Serveranfragen um bis zu 80% bei wiederholten Besuchen

const CACHE_NAME = 'sonja-portfolio-v1';
const urlsToCache = [
    '/css/styles.css',
    '/js/script.js',
    '/index.html',
    '/about.html'
];

// Installation - Dateien cachen
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('✅ Cache geöffnet');
                return cache.addAll(urlsToCache);
            })
    );
});

// Fetch - Aus Cache laden wenn verfügbar
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Cache hit - gebe gecachte Version zurück
                if (response) {
                    return response;
                }
                
                // Nicht im Cache - hole vom Server
                return fetch(event.request).then(response => {
                    // Prüfen ob gültige Response
                    if (!response || response.status !== 200 || response.type !== 'basic') {
                        return response;
                    }
                    
                    // Clone für Cache
                    const responseToCache = response.clone();
                    
                    caches.open(CACHE_NAME)
                        .then(cache => {
                            cache.put(event.request, responseToCache);
                        });
                    
                    return response;
                });
            })
    );
});

// Aktivierung - Alte Caches löschen
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('🗑️ Alten Cache löschen:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
