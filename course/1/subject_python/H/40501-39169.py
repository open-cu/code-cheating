n = 0
k = 0


def isPalindrome(s):
    rev = "".join(reversed(s))
    if s == rev:
        return "Yes"
    return "No"


s = input()
s_rev = "".join(reversed(s))
for letter in range(len(s)):
    if s[letter] == "a":
        n += 1
    if s[letter] != "a":
        break
for letter in range(len(s)):
    if s_rev[letter] == "a":
        k += 1
    if s_rev[letter] != "a":
        break
if n > k:
    print("No")
else:
    print(isPalindrome(s[n: (len(s) - k)]))
