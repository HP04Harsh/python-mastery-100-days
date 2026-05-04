# Simple restaurant menu project
menu = {
    1: ("Burger", 5.99),
    2: ("Fries", 2.99),
    3: ("Soda", 1.5),
    4: ("Salad", 4.5)
}

print("Menu:")
for k, v in menu.items():
    print(k, ":", v[0], "- $", v[1])

order = []
while True:
    choice = input("Enter item number to add (or 'done'): ")
    if choice.lower() == 'done':
        break
    try:
        idx = int(choice)
        if idx in menu:
            order.append(menu[idx][1])
            print(menu[idx][0], "added.")
        else:
            print("Invalid item.")
    except ValueError:
        print("Please enter a number or 'done'.")

total = sum(order)
print(f"Total amount: ${total:.2f}")
