# Find maximum and minimum from input numbers
count = int(input("How many numbers? "))
if count <= 0:
    print("No numbers provided.")
else:
    first = float(input("Enter number 1: "))
    current_max = current_min = first

    for i in range(1, count):
        val = float(input(f"Enter number {i+1}: "))
        if val > current_max:
            current_max = val
        if val < current_min:
            current_min = val

    print("Maximum:", current_max)
    print("Minimum:", current_min)
