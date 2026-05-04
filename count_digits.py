# Count digits in a number
num = int(input("Enter a number: "))
n = abs(num)
count = 0

if n == 0:
    count = 1
else:
    while n != 0:
        n //= 10
        count += 1

print("Number of digits:", count)
