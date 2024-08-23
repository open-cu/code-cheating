word = input()
lpoint = 0
rpoint = 1
new_word = ''
end = True
while end:
    if word[lpoint:rpoint].isnumeric():
        rpoint += 1
        continue
    else:
        new_word += word[rpoint - 1] * (1 if lpoint + 1 == rpoint else int(word[lpoint:rpoint - 1]))
        lpoint = rpoint
        rpoint += 1

    if rpoint > len(word):
        end = False
print(new_word)
