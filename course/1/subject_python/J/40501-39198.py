input()
nums = [int(x) for x in input().split()]
while len(nums) != 1:
    while nums[1]:
        nums[0], nums[1] = nums[1], nums[0] % nums[1]
    nums.pop(1)
print(nums[0])