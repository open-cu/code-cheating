compressed_string = input()
uncompressed_string = ""
multiplier = 1
for i in compressed_string:
    if i.isalpha():
        multiplier = int(multiplier)
        uncompressed_string += multiplier * i
        multiplier = 1
    elif multiplier == 1:
        multiplier = i
    else:
        multiplier += i
print(uncompressed_string)
