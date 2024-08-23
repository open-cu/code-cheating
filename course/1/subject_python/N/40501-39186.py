def can_read_word(circle, word):
    for i in range(len(circle)):
        valid_start = True
        for j in range(len(word)):
            if circle[(i + j) % len(circle)] != word[j]:
                valid_start = False
                break
        if valid_start:
            return True
    return False


circle = input()
word = input()

res = can_read_word(circle, word)
res_reverse = can_read_word(circle[::-1], word)

print('Yes' if res or res_reverse else 'No')
