const CACHE="kingfront-v0.96.0";
const SHELL=["./","./index.html","./manifest.webmanifest","./assets/icon-192.png","./assets/icon-512.png","./assets/apple-touch-icon.png"];
self.addEventListener("install",event=>{event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(SHELL)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>key.startsWith("kingfront-v")&&key!==CACHE).map(key=>caches.delete(key)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",event=>{if(event.request.method!=="GET")return;event.respondWith(caches.match(event.request).then(hit=>hit||fetch(event.request).then(resp=>{if(!resp||resp.status!==200||resp.type==="opaque")return resp;const copy=resp.clone();caches.open(CACHE).then(cache=>cache.put(event.request,copy));return resp}).catch(()=>caches.match("./index.html"))))});
