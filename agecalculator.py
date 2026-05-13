from datetime import date

def age(dob):
    today = date.today()

    years = today.year-dob.year
    
    if (today.month,today.day) < (dob.month,dob.year):
        years -=1
    return years

print(age(date(2002,4,9)))        
