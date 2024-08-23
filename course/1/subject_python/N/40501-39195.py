def is_in(line: str, word: str):
    i = 0
    for c in word:
        if line[i] != c:
            return False
        i = (i + 1) % len(line)

    return True


def is_in_circle(circle: str, word: str):
    anchor = circle.find(word[0])

    clkwise = circle[anchor:] + circle[:anchor]
    cntr_clkwise = circle[anchor::-1] + circle[:anchor:-1]

    return is_in(clkwise, word) + is_in(cntr_clkwise, word) > 0


def solution():
    circle = input()
    word = input()

    print("YES" if is_in_circle(circle, word) else "NO")


solution()
