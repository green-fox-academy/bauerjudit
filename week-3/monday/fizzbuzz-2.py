a = 0

while a < 100:
    if a % 3 == 0 and a % 5 == 0:
        print("fizzbuzz")
    elif "3" in str(a):
        print("fizz")
    elif "5" in str(a):
        print("buzz")
    elif a % 3 == 0:
        print("fizz")
    elif a % 5 == 0:
        print("buzz")
    else:
        print(a)
    a+=1
