from threading import *
from time import *

def display(str):
    l.acquire()
    for x in str:
        print(x)

    l.release()

l = Lock()        


t1 = Thread(target=display,args=('Harsh Pardhi',))
t2 = Thread(target=display,args=('Sakshi Rokde',))

t1.start()
t2.start()

t1.join()
t2.join()