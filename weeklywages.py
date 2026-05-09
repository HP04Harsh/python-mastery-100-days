hours =[8, 10, 8, 7, 11]
wage  = 40

week_hours = [ x for x in hours]
total_hours = sum(week_hours)


if total_hours<=40:
    totalwage = total_hours * wage
    print(totalwage)

else:
    overtime = total_hours - 40
    totalwage = (overtime * wage * 1.2) + (wage * 40)
    print(totalwage)