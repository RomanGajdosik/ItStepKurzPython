#??  Verzia 1 
# import threading
# import time

# def background_task():
#     while True:
#         print("Daemon thread is running...")
#         time.sleep(2)

# daemon_thread = threading.Thread(target=background_task, args=(), daemon=True)
# daemon_thread.start()

# print("Zacni program")
# time.sleep(11)
# print("Ukonci program")\
import time
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def download_site(url):
    print("Stahujem... " + url)
    with urllib.request.urlopen(url) as response:
        return f"Stiahnutie {url}: {len(response.read())} bytov"

sites = [
    "http://www.example.com",
    "http://www.example.org",
    "http://www.example.net",
]

start_time = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    for site in sites:
        futures.append(executor.submit(download_site, site))

    for future in futures:
        result = future.result()
        print(result)

duration = time.time() - start_time
print(f"Stiahnuté {len(sites)} stránok za {duration} sekúnd")
