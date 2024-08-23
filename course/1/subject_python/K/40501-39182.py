string = list(input())
result = ''
numbers = ''
for i in range(len(string)-1):
    if string[i].isdigit() and string[i+1].isalpha():
        numbers += string[i]
        string[i] = string[i+1] * (int(numbers) - 1)
        i += 1
        numbers = ''
    elif string[i].isdigit():
        numbers += string[i]

for i in string:
    if i.isdigit():
        del string[string.index(i)]

for i in string:
    result += i
print(result)