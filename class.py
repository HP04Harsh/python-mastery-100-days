class Test:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
         return self.l * self.b    

    def show(self):
        print(f"Total area of {self.l} and {self.b} is {self.area()}")


arr = Test(10,15)            
arr.area()
arr.show()