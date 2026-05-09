import re as regex 


def pangram(str):
    letter = regex.sub(r'[^a-zA-Z]','',str)
    letter_set = set(letter.lower())

    if len(letter_set)==26:
        return True
    else:
        return False    

str = 'The quick brown fox dog'

print(pangram(str))  