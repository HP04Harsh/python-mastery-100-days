import itertools as it

alphas = ['a','b','c','d','e']

perm = it.permutations(alphas,r=2)
permutation = list(perm)

print(permutation)