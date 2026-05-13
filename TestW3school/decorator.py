def Outer(f):
    def Inner():
         print("*"*10)
         f()
         print("*"*10)
    return Inner()

@Outer
def display():
    print("CEO Harsh Pardhi")


display           