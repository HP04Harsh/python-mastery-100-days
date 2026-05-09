import re as regex

pattern = r'[a-z]+\.(com|in)$'
domain = "udemy.com"

if regex.fullmatch(pattern, domain):
    print("Domain is valid")
else:
    print("Domain Not valid")    