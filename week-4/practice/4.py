filename = "alma"


def wc(filename):
input_file = open(filename)
file_content = input_file.read()
line_count = len(file_content.split("\n"))
input_file.close()
return [line_count, len(file_content)]

print(wc(filename))











"""new_file = open("alma.txt", "w")


lines = new_file.read()

def wc(filename):
    line_count = 0
    for char in words:
        if char == "\n":
            line_count += 1
    return line_count

    char_count = filename.count("")
    return char_count


    for char in words:
        char_count = 0
        char_count + = 1
        return char_count

print(wc(filename))

# line
# char
new_file.write("alamabjhvcliewhvfireobvjlregfoe")
new_file.close"""
