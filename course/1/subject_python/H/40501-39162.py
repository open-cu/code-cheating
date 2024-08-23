def is_palindrome(string):
    return string == string[::-1]


string = input()

count_of_letters_a_start = 0
for letter in string:
    if letter == "a":
        count_of_letters_a_start += 1
    else:
        break


count_of_letters_a_finish = 0
for letter in string[::-1]:
    if letter == "a":
        count_of_letters_a_finish += 1
    else:
        break

if (
    count_of_letters_a_finish == 0 and is_palindrome(string) or count_of_letters_a_finish != 0 and is_palindrome(
        string[count_of_letters_a_start:-count_of_letters_a_finish]
    ) and count_of_letters_a_start <= count_of_letters_a_finish
):
    print("YES")
else:
    print("NO")
