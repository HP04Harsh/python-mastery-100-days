class A:
    def __init__(self):
        self.inner_obj = self.Inner()

    class Inner:
        def __init__(self):
            self.data = "Inner Data"    
        def show(self):
            print(self.data)


r = A()
print(r.inner_obj.show())              