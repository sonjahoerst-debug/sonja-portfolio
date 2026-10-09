// Service Worker für nachhaltiges Caching
// Strategie: Netzwerk zuerst (immer aktuelle Inhalte), Cache nur als Offline-Fallback

const CACHE_NAME = 'sonja-portfolio-v6';
const urlsToCache = [
    '/css/styles.css',
    '/js/script.js',
    '/index.html',
    '/about.html'
];

// Installation - Dateien cachen und sofort aktivieren
self.addEventListener('install', event => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
    );
});

// Fetch - nur GET-Anfragen der eigenen Domain behandeln
self.addEventListener('fetch', event => {
    const request = event.request;
    if (request.method !== 'GET' || new URL(request.url).origin !== self.location.origin) {
        return;
    }
    // Videos (Range-Requests) nicht über den Cache leiten
    if (request.headers.has('range')) {
        return;
    }

    event.respondWith(
        fetch(request)
            .then(response => {
                if (response && response.status === 200 && response.type === 'basic') {
                    const copy = response.clone();
                    caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
                }
                return response;
            })
            .catch(() => caches.match(request))
    );
});

// Aktivierung - alte Caches löschen und Kontrolle übernehmen
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys()
            .then(names => Promise.all(
                names.filter(name => name !== CACHE_NAME).map(name => caches.delete(name))
            ))
            .then(() => self.clients.claim())
    );
});
