def its_life(text: str) -> str:
    new_text = []
    digit = ''
    i = 0
    while i < len(text):
        if text[i].isalpha():
            new_text.append(text[i])
            i += 1
        else:
            digit = ''
            while i < len(text) and text[i].isdigit():
                digit += text[i]
                i += 1
            if digit:
                new_text.append(text[i] * (int(digit) - 1))
    result = ''.join(new_text)
    return result


test = input()
print(its_life(test))
