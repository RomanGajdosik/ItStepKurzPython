import urllib.request
import time
import threading


def download_site(url):
    with urllib.request.urlopen(url) as response:
        print(f"Stiahnutie {url}: {len(response.read())} bytov")

sites = [
    "http://www.zsr.sk/",
    "http://www.google.com",
    "http://httpforever.com",
    
]
threads =[]
start_time = time.time()
for site in sites:
    thread = threading.Thread(target = download_site, args=(site,))
    threads.append(thread)
    thread.start()

for thread in threads:
    
    thread.join()
    
duration = time.time() - start_time
print(f"Stiahnuté {len(sites)} stránok za {duration} sekúnd")