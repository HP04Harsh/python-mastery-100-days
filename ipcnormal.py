from threading import Thread, Condition

class Data:
    def __init__(self):
        self.data = 0
        self.cv = Condition()

    def put(self, value):
        with self.cv:
            self.data = value
            print("Produced:", value)
            self.cv.notify()   # Consumer ko signal

    def get(self):
        with self.cv:
            self.cv.wait()     # Producer ka wait
            print("Consumed:", self.data)

obj = Data()

def producer():
    for i in range(1, 6):
        obj.put(i)

def consumer():
    for _ in range(5):
        obj.get()

t1 = Thread(target=producer)
t2 = Thread(target=consumer)

t1.start()
t2.start()