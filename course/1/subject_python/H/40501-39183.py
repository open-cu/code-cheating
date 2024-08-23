def poly_check(poly: str) -> str:
    left = 0
    right = len(poly) - 1
    counter = 0
    while right - left > 0:
        if poly[left - 1] != 'a':
            counter = 1
        if poly[right] != poly[left]:
            if poly[right] != 'a' or counter > 0:
                return 'No'
            else:
                right -= 1
        else:
            right -= 1
            left += 1
    return 'Yes'


string = input()
print(poly_check(string))
