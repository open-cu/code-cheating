string = input()
string_lst = []
number = ''

for i in range(len(string)):
    if string[i].isdigit() and string[i+1].isdigit():
        number += string[i]
    elif string[i].isdigit() and not string[i+1].isdigit():
        number += string[i]
        string_lst.append(number)
        number = ''
    else:
        string_lst.append(string[i])
    
for i in range(len(string_lst)):
    string_lst[i] = (int(string_lst[i])-1) * string_lst[i+1] if string_lst[i].isdigit() else string_lst[i]
    
print(''.join(string_lst))