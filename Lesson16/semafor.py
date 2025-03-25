import threading
import time

# Vytvorenie semaforu s dvomi povoleniami
semaphore = threading.Semaphore(2)

def access_resource(i):
    print(f'Vlakno {i} sa pokusa ziskat semafor.')
    semaphore.acquire()  # Ziskat povolenie
    print(f'Vlakno {i} vstupilo do kritickej sekcie.')
    time.sleep(1)  # Simulacia prace
    print(f'Vlakno {i} odchadza z kritickej sekcie.')
    semaphore.release()  # Uvolnit povolenie

threads = []
for i in range(10):
    threads.append(threading.Thread(target=access_resource, args=(i,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
