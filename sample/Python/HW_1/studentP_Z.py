n1 = 10
n2 = 100

minimum = min(n1, n2)

print(f"The minimum number is {minimum}")

nums = [1, 2, 3, 4, 5]

total = sum(nums)
length = len(nums)

average = total / length

print(f"The average of {nums} is {average}")

# A function that checks if a year is a leap year
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Example
year = 2020

if is_leap(year):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")