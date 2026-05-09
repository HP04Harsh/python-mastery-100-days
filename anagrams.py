s1 = "harsh"
s2= "pardhi"

if len(s1)!=len(s2):
    print("Not Anagram")

else:
    for x in s1:
          if S1.count(x) != S2.count(x):
              print("Not Anagram")
              break
    else:
        print("Anagram")

