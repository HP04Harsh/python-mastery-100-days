# Sum of N numbers
n = int(input("How many numbers to sum? "))
total = 0
for i in range(n):
    value = float(input(f"Enter number {i+1}: "))
    total += value

print("Total sum:", total)
