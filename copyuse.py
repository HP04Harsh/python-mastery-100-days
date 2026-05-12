import copy

L1 = [10,20,30,40,50]
L2 = copy.copy(L1)

print(id(L1[2]))
print(id(L2[2]))