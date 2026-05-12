import csv

data = [
    [101,'Harsh','Gondia'],
    [102,'Sakshi','Nagpur']
]

with open('student.csv','r',newline='') as file:
    mywriter = csv.DictReader(file)
    for data in mywriter:
        print(data)
