# Fibonacci series up to n terms
n = int(input("How many Fibonacci terms? "))
if n <= 0:
    print("Provide a positive integer.")
elif n == 1:
    print("0")
else:
    a, b = 0, 1
    seq = [a, b]
    for _ in range(2, n):
        a, b = b, a + b
        seq.append(b)
    print(" ".join(str(x) for x in seq))
