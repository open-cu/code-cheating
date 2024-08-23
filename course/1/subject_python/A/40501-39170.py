def check_string(text: str) -> str:
    if (text[0].isalpha() and text[1].isdigit()) or (text[1].isalpha() and text[0].isdigit()):
        return 'YES'
    else:
        return 'NO'


test = input()
print(check_string(test))
