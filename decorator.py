def Outer(f):
    def Inner():
        print("*" * 10)

        f()
        
        print("*" * 10)

    return Inner 

@Outer
def display():
   return print("Hello Gondia")

display()