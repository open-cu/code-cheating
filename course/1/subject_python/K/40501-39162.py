def scan_number(string, start_index):
    number = ""

    while start_index < len(string):
        if string[start_index].isdigit():
            number += string[start_index]
            start_index += 1
        else:
            return int(number), start_index


string = input()

index = 0

string_result = ""

while index < len(string):
    if string[index].isdigit():
        number, new_index = scan_number(string, index)
        string_result += string[new_index] * number
        index = new_index + 1
    else:
        string_result += string[index]
        index += 1

print(string_result)
