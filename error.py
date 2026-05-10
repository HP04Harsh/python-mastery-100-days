def division(a,b):
    if b==0:
        raise ZeroDivisionError
    else:
        return a/b 

try:
    result = division(10,10)
    print(result)
except ZeroDivisionError:
    print("Cannot Divide by Zero")
