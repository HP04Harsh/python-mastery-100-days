class Rect:

    count = 0

    def __init__(self,a,b):
        self.a = a 
        self.b = b
        Rect.count+=1

    def area(self):
        return self.a*self.b

    def perimeter(self):
        return 2*(self.a + self.b)        

    
    def get_count(l,b):
        return l*b    

r1 = Rect(10,15)        
print(r1.area())
print(r1.perimeter())
print(r1.get_count(10,150))