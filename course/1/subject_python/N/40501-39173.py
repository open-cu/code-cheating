chain = input()
word = input()
chain_multiplier = max(len(chain), len(word)) // min(len(chain), len(word)) + 1
if word in chain * chain_multiplier or word in chain[::-1] * chain_multiplier:
    print('YES')
else:
    print('NO')