n = int(input())
nums = [abs(int(x)) for x in input().split()]
min_ind_left = nums.index(min(nums))
min_ind_right = n - nums[::-1].index(min(nums)) - 1
ansflg = True
for i in range(1, min_ind_left):
    if nums[i - 1] < nums[i]:
        ansflg = False
        break
if ansflg:
    for i in range(min_ind_right + 1, n):
        if nums[i - 1] > nums[i]:
            ansflg = False
            break
print('Yes' if ansflg else 'No')
if ansflg:
    print(' '.join([str(-x) for i, x in enumerate(nums) if i < min_ind_left] + [str(x) for i, x in enumerate(nums) if
                                                                                i >= min_ind_left]))
