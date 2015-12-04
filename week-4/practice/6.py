filename = "alma.txt"

def add_a(text):
    new_text = (open(text)).read()
    new_text.close()
    split_text = new_text.split("\n")
    output = ""
    for line in split_text:
        output += line + "A" + "\n"
    return output


def add_a(text):
    new_text = (open(text)).readlines()
    new_text.close()
    output = ""
    for line in new_text:
        print("a" + line.rstrip)
