a = int(input())
nums = input()
nums_l = nums.split(' ')
nums_list = []

for i in nums_l:
    nums_list.append(int(i))


def evklid(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return (x + y)


if a == 1:
    print(nums_l[0])
else:
    nod = evklid(nums_list[0], nums_list[1])

    for i in range(a - 2):
        nod = evklid(nod, nums_list[2 + i])

    print(nod)
