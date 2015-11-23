num = 4


if num == 0 or num == 1:
        print("not prim")
for x in range(2, num):
    if num % x == 0:
        print("not prim")
        break
    else:
        print("prim")
        break
