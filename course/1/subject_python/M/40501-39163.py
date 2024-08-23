n = int(input())
a = input().split(" ")
arr = [int(i) for i in a]
new_arr = []
check_if_all_ones = 0
# if arr[1] == 1:
#    new_arr.append(1)
start = 1
'''
while start < n:
    if arr[start] == 1:
        new_arr.append(1)
        start += 1
    else:
        break
        '''
counter = arr.count(1)
for i in range(1, n):
    if arr[i - 1] >= arr[i]:
        new_arr.append(arr[i - 1])
    # if arr[-1] == 1 and n != 1:
    #    counter += 1
if len(arr) == 2 and arr[0] == 1 and arr[-1] == 1:
    counter = 2
for i in arr:
    if i == 1:
        check_if_all_ones += 1
if n == check_if_all_ones:
    counter = n
    new_arr = arr[:-1]
new_arr.append(arr[-1])
print(counter)
print(*new_arr)
