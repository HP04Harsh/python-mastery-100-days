from threading import Thread
from queue import Queue


q = Queue()

def producer():
    for i in range(1,5):
        q.put(i)
        print(f"Producer: {i}")

def consumer():
    while True:
        result = q.get()       
        print(result) 


t1 = Thread(target=producer,name='Producer')
t2 = Thread(target=consumer,name='Consumer')

t1.start()
t2.start()

t1.join()
t2.join()