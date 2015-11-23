i = 0
b = 0
a = 1
fibonacci = []
print(b)
print(a)

while i < 5:
    x = b + a
    b = a
    a = x
    print(a)
    fibonacci.append(a)
    i+=1
print(fibonacci)
