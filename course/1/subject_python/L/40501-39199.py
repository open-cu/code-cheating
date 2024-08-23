def can_be_increasing(nums):
    if nums[0] > 0:
        nums[0] *= -1

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            nums[i] = -nums[i]
            if nums[i] < nums[i - 1]:
                return False

        if nums[i] > 0 and -nums[i] >= nums[i - 1]:
            nums[i] *= -1

    return True


_ = input()
nums = list(map(int, input().split()))
if can_be_increasing(nums):
    print("Yes")
    print(*nums)
else:
    print("No")
