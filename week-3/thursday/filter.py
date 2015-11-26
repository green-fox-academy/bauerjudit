numbers = [1, 2, 3, 4, 5, 6, 7, 8]
output = []


for n in numbers:
    if n % 2 == 0:
        output.append(n)

print(output)


i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        output.append(numbers[i])
    i += 1
print(output)


def filter_even():
    for n in numbers:
        if n % 2 == 0:
            output.append(n)
filter_even()

print(output)


def filter_even(unfilteres_list):
    output = []
    for n in unfiltered_list:
        if n % 2 == 0:
            output.append(n)
    return output

output = filter_even(numbers)

print(output)
