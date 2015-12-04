filename = "alma.txt"

def print_file(text):
    new_file = (open(text)).read()
    text.close()
    return new_file




"""return (open(text)).read()
opened_file = open(text)
new_file = opened_file.read()
return new_file"""
