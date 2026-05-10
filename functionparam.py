def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y


def division(x,y):
    return x/y

def arithmetic(f,x,y):
    return f(x,y)

print(arithmetic(multiply,10,15))               