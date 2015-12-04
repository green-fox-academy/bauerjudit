numbers = [3, 4, 5, 6, 7]


def reverse(nums):
    output = []
    for num in nums[::-1]:
        output.append(num)
    return output

print(reverse(numbers))




def reverse2(nums):
    output = []
    i = len(nums)-1
    while i >= 0:
        output.append(nums[i])
        i -= 1
    return output

print(reverse2(numbers))
