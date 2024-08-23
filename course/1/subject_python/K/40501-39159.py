s = input()

uncompressed = ''
mult = ''
for letter in s:
    if ('0' <= letter <= '9'):
        mult += letter
    elif (len(mult) > 0):
        uncompressed += letter * int(mult)
        mult = ''
    else:
        uncompressed += letter

print(uncompressed)
