

def list_items():
    text = (open("todo.txt", "r")).readlines()
    for index, line in enumerate(text):
        print(index + 1, line)

#list_items()


def add_item():
    text = open("todo.txt", "a")
    user_input = input("Add a new item: ")
    text.write(user_input)

#add_item()


def remove_item():
    text = (open("todo.txt", "r")).readlines()
    user_input =int(input("Which one do you want to remove? Add a number: "))
    ask = input("Are you sure? Y/N? ").lower()
    text_write = (open("todo.txt", "w"))
    if ask == "y":
        del text[user_input-1]
        for line in text:
            text_write.write(line)
        text_write.close()
    elif ask == "n":
        return menu()
    else:
        return menu()

#remove_item()
