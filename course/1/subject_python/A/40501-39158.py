string_input = input()


def check_string(string):

    flag_letter = False
    flag_number = False

    for char in string:

        if char.isalpha():
            flag_letter = True

        if char.isdigit():
            flag_number = True

    return 'YES' if flag_letter and flag_number else 'NO'


print(check_string(string_input))
