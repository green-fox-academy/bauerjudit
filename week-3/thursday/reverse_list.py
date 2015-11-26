numbers = [1, 2, 3, 4]

def reverse():
    output = []
    i = len(numbers)-1
    while i >= 0 :
        output.append(numbers[i])
        i -= 1
    return output

print(reverse())


def reverse():
    output = []
    i = len(numbers)
    for n in range(i, 0, -1):

        output.append(n)
    return output

print(reverse())
