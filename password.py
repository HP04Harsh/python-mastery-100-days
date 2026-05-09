'''Given two password strings, determine whether they:
Match exactly
Match only in a case-insensitive comparison
Do not match at all'''

pwd1 = "Harsh"
pwd2 = "harsh"

if pwd1==pwd2:
    print("password matches")
elif pwd1.casefold()!= pwd2.casefold():
    print("Password cases not matches")
else:
    print("Please check password")
