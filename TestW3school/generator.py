def display():
    for i in range(1,10):
      yield i


gen = display()

print(next(gen))
