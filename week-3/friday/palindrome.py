def reverse(my_string):
    reversed_string = ""
    for char in my_string:
        reversed_string = char + reversed_string
    return reversed_string

def make_palindrome(from_string):
    return from_string + reverse(from_string)

def lets_play():
    user_input = input("Enter a word: ").lower()
    swear_words = ["python", "kutyafaja"]

    try:
        if user_input in swear_words:
            raise ValueError
        print(make_palindrome(user_input))

    except ValueError:
        print("Heeey watch out!")
lets_play()
