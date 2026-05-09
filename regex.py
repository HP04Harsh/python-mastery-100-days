import re as regex

text = "Hello how are Hello you"

print(regex.findall("(h)+",text))