n = int(input())
array = list(map(int, input().split()))
value_check = -abs(max(array, key=abs))
success_flag = True
for i in range(n):
    array[i] = abs(array[i])
    if -array[i] >= value_check:
        array[i] = -array[i]
    elif array[i] < value_check:
        print("No")
        success_flag = False
        break
    value_check = array[i]

if success_flag:
    print("Yes")
    print(*array)
