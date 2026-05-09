import re as regex

pattern = r'\w+\.?\w+\@\w+\.(com|org)\Z'
email = "harshpardhi477@gmail.com"

if regex.fullmatch(pattern,email):
    print("Valid email")
else:
    print("No Valid")    