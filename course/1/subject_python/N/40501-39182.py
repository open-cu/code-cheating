nabor_bukv = input()
slovo = input()

nabory = nabor_bukv * 2

if len(slovo) <= len(nabor_bukv):
    if slovo in nabory:
        print('Yes')
    elif slovo[::-1] in nabory:
        print('Yes')
    else:
        print('No')

k = 0
if len(slovo) > len(nabor_bukv):
    k = len(slovo) // len(nabor_bukv) + 1
    nabory = nabor_bukv * k
    if slovo in nabory:
        print('Yes')
    elif slovo[::-1] in nabory:
        print('Yes')
    else:
        print('No')