my_file = open("duplicated_chars.txt", "r")

lines = my_file.readlines()

for char in lines:
    print(char[::2], end="")





my_file.close()
