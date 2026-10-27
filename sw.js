// TadilatMaliyeti.com - Offline-First Service Worker (Mandate v9.1)
const CACHE_NAME = 'tadilatmaliyeti-v9.1';
const PRECACHE_URLS = [
  '/',
  '/hesapla',
  '/banyo-tadilati-maliyeti',
  '/mutfak-yenileme-fiyatlari',
  '/komple-ev-tadilati-fiyatlari',
  '/izmir-ev-tadilati-fiyatlari',
  '/tadilat-sozlesmesi-ve-sartname-ornegi',
  '/sik-sorulan-sorular',
  '/favicon.ico',
  '/site.webmanifest'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(PRECACHE_URLS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    fetch(event.request)
      .catch(() => caches.match(event.request))
  );
});
