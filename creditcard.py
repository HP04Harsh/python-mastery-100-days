cardno = input("Enter the card no.: ")
lastdigit= cardno[15:]
four = 'X' * 4 + ' '
DispNo = four *3 + lastdigit

print(DispNo)