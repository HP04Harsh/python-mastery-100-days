class Rect:

    def __init__(self,l,b):
        self.l = l 
        self.b = b 

    def area(self):
        return self.a * self.b 


class Cuboid(Rect):

    def __init__(self,l,b,h):
        self.h = h 
        super().__init__(l,b)

    def volume(self):
        return self.h * self.l * self.b 

cube = Cuboid(10,5,6)
print(cube.volume())