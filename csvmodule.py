import csv

fields = ['Name','Age','City']

data = [
    {"Name": "Harsh", "Age": 21, "City": "Nagpur"},
    {"Name": "Sakshi", "Age": 21, "City": "Gondia"}
]

with open('student.csv','r',newline='') as file:
    mydata = csv.DictReader(file)
    for rows in mydata:
        print(rows[Name])
   
    
