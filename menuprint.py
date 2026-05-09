item = input("Enter your dish name: ")
cost = input("Cost of an item: ")
dash = 20-len(item)-len(cost)

print(item  +('-'*dash) + cost)