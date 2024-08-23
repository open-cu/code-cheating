nums = [1, 1]
i = int(input())
for _ in range(i - 2):
    nums.append(nums[-2] + nums[-1])
print(nums[i - 1])