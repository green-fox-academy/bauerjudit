my_file = open("reversed_zen_lines.txt", "r")

while True:
    line = my_file.readline()
    if not line:
        break
    print(line[::-1], end='')


# lines = my_file.readlines()
#
# for line in lines:
#     print(line[::-1], end='')
