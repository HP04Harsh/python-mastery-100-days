import re


str1 = ('a once')
str2 = ("a once")

word1 = re.findall(r'\w+',str1.lower())
word2 = re.findall(r'\w+',str2.lower())

wset1 = set(word1)
wset2 = set(word2)

union = wset1 | wset2
intersection = wset1 & wset2
plagiarism_score = len(intersection)/len(union)

if plagiarism_score >= 0.50:
    print("Highly Plagiarism")
else:
    print("Human Write")    