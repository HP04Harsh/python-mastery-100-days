scan = r'These+notes#reveal9Newton seeking-out an{underlying structure to/the\pyramid}'
clean = ''

for z in scan:
    if z.isalpha() or z.isspace():
        clean = clean + z
    else:
        clean = clean + ' '


print(clean)        