my_file = open("encoded_zen_lines.txt", "r")
new_file = open("bob_ross.txt", "w")

lines = my_file.readlines()

for line in lines:
    words = line.split(" ")
    decoded_line = []
    for word in words:
        decoded_word = ""
        for char in word:
            decoded_word += chr(ord(char)-1)
        decoded_line.append(decoded_word)
    #print(" ".join(decoded_line))


    new_file.write(" ".join(decoded_line)+ "\n")

my_file.close()
new_file.close()
