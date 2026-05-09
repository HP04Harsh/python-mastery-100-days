def myfunc(n):
    i =0
    while i<n:
        yield i  # this is generator
        i+=1

test = myfunc(5)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))