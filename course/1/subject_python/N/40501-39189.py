s1 = input()
s2 = input()

circle = s1 * (len(s1) // len(s2) + 3)
print("YES" if s2 in circle or s2 in circle[::-1] else "NO")
