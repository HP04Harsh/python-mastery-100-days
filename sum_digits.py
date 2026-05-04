# Sum of digits of a number
num = int(input("Enter a number: "))
n = abs(num)
sum_digits = 0

while n != 0:
    sum_digits += n % 10
    n //= 10

print("Sum of digits:", sum_digits)
