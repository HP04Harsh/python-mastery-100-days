# Reverse a number
num = int(input("Enter a number: "))
n = abs(num)
rev = 0

while n != 0:
    rev = rev * 10 + (n % 10)
    n //= 10

if num < 0:
    rev = -rev

print("Reversed number:", rev)
