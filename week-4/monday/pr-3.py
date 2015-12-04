l = 3

def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num -1) * num

print(factorial(l))




def factorial1(num):
    output = 1
    i = 1
    while i <= num:
        output *= i
        i += 1
    return output

l = factorial1(l)
print(l)




def factorial2(num):
    output = 1
    for n in range(1, num + 1):
        output *= n
    return output



l = factorial2(l)
print(l)
