word = input()
new_word = ""
i = 0
while i < len(word):
    if word[i].isdigit() and word[i + 1].isdigit():
        count = int(word[i] + word[i + 1])
        new_word += word[i + 2] * count
        i += 3
    elif word[i].isdigit() and word[i + 1].isdigit() is False:
        count = int(word[i])
        new_word += word[i + 1] * count
        i += 2
    else:
        new_word += word[i]
        i += 1
print(new_word)
