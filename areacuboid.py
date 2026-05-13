def area(l,b,h):
    def area(d1,d2):
        return d1*d2

    return 2 * area(l,b) + area(b,h) + area(l,h)

print(area(10,5,3))