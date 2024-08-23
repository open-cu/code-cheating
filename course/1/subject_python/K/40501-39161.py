s = input()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

i = 0
counter = ''
number_condition = False
new_string = ''

for el in s:
    if el in numbers:
        counter = counter + el
        number_condition = True
    elif number_condition and el not in numbers:
        number_condition = False
        new_string = new_string + el * int(counter)
        counter = ''
    else:
        new_string = new_string + el

print(new_string)
