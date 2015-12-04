








my_file = open("reversed_zen_order.txt", "r")

lines = my_file.readlines()

my_file.close()

reversed_lines = lines[::-1]

#print(reversed_lines)

for line in reversed_lines:
    print(line, end='')
