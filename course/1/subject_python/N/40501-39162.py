circle = input()
word = input()


def check_in_circle(circle, word):
    if circle < word:
        circle = circle * (len(word) // len(circle) + 1)
    for i in range(len(word)):
        temp_circle = circle[-i:] + circle[:-i]
        if word in temp_circle:
            return True
    return False


if check_in_circle(circle, word) or check_in_circle(circle[::-1], word):
    print("YES")
else:
    print("NO")
