import threading
import random

def find_largest(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    print(f"Najvacsi clen:{largest}")
def find_smallest(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    print(f"Najmensi clen:{smallest}")
mnoz=[]    
for i in range(1,100000):
    mnoz.append(int(i))
random.shuffle(mnoz)
print(mnoz)
thread1 = threading.Thread(target=find_largest, args=(mnoz,))
thread2 = threading.Thread(target=find_smallest, args=(mnoz,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('Vlakna ukoncili vykonavanie')
