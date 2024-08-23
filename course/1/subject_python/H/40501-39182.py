string = input()
# print(string)
counter_start = 0
for i in range(len(string)):
    if string[i] == 'a':
        counter_start += 1
    else:
        break
# print('a'* counter_start)

string_reverse = string[::-1]
# print(string_reverse)
counter_end = 0
for i in range(len(string_reverse)):
    if string_reverse[i] == 'a':
        counter_end += 1
    else:
        break
# print('a'* counter_end)

if counter_end < counter_start:
    print('No')
else:
    string_new = 'a'*(counter_end - counter_start) + string
    # print(string_new)
    if string_new[::-1] == string_new:
        print('Yes')
    else:
        print('No')