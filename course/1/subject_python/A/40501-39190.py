inputStr = input()
hasDigit = inputStr[0].isnumeric() or inputStr[1].isnumeric()
hasLetter = inputStr[0].isalpha() or inputStr[1].isalpha()

print('YES' if hasDigit and hasLetter else 'NO')
