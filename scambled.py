word_set = {'plea', 'medical', 'listen', 'leap', 'decimal', 'silent', 'pale', 'enlist'}

result = set()

for words1 in word_set:
    for words2 in word_set:
        if words1!=words2 and sorted(words1)==sorted(words2):
            pair = tuple(sorted((words1,words2)))
            result.add(pair) 
print(result)                      
