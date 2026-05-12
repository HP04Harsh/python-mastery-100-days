from collections import deque

L= [1,2,3,4,5,6,7,8,9]
d = deque(L)
d.appendleft(11)
print(type(d))
