import re as regex

name_pattern = r'[A-Z][a-z]+ [A-Z][a-z]+'
name = "harsh Pardhi"

if regex.fullmatch(name_pattern,name):
    print("Name matched the pattern")
else:
    print("Name not matched")       