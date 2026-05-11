class Test:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    @property
    def length(self):
        return self._l

    @length.setter
    def length(self, value):
        if value >= 0:
            self._l = value
        else:
            self._l = 1

    @property
    def breadth(self):
        return self._b

    @breadth.setter
    def breadth(self, value):
        if value >= 0:
            self._b = value
        else:
            self._b = 1

    def area(self):
        return self._l * self._b


ar = Test(10, 10)
print(ar.area())