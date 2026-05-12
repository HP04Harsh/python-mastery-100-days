from collections import Counter 

names = ["Mark", "Johnny", "Mark", "David", "Mark", "Johnny"]
c = Counter(names)
c.update({"Harsh":5})
print(c.values())