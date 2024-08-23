# ввод
s = input()

new_string = ''
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

i = 0
while i < len(s):
    if s[i] in numbers:
        temp = ''
        while s[i] in numbers:
            temp += s[i]
            i += 1
        new_string += int(temp) * s[i]
    else:
        new_string += s[i]
    i += 1

print(new_string)
