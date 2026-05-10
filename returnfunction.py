def Outer():
    def Inner():
        return print("Welcome Gondia")
    return Inner
f = Outer()
f()   
