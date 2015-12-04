numbers = [3, 4, 5, 6, 7]

def filter(my_list):
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(filter(numbers))


def filter2(my_list):
    new_list = []
    i = 0
    while  i > len(my_list)-1:
        if my_list[i] % 2 == 0:
            new_list.append(my_list[i])
    i += 1
    return new_list

print(filter2(numbers))
