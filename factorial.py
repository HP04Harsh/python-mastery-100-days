# Factorial of a given number
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial not defined for negative numbers.")
else:
    result = 1
    for i in range(2, n+1):
        result *= i
    print(f"{n}! =", result)
