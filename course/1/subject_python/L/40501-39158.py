n = int(input())
numbers = [int(x) for x in input().split(" ")]


def descending_array(nums, array):
    result = [min(array[0], -array[0])]

    flag = True

    for i in range(1, nums):
        temp = result[-1]

        positive = array[i]
        negative = -array[i]

        if positive >= temp and negative >= temp:
            result.append(min(positive, negative))
        elif positive >= temp:
            result.append(positive)
        elif negative >= temp:
            result.append(negative)
        else:
            flag = False
            return result, flag

    return result, flag


output, flag = descending_array(n, numbers)

if flag:
    print("Yes")
    print(" ".join(map(str, output)))
else:
    print("No")
