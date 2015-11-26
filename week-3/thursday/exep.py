from random import randint

def get_integer():
    number = int(input("guess a number between 1-10: "))
    return number

computer = randint(1, 10)

number_of_guesses = 5

while number_of_guesses > 0:
    try:
        guess = get_integer()
    except ValueError:
        print("You entered a wrong value")
    else:
        if computer == guess:
            print("you win")
            break
        elif computer > guess:
            number_of_guesses -= 1
            print("guess bigger")
        else:
            computer < guess
            number_of_guesses -= 1
            print("guess smaller")
        if number_of_guesses == 0:
            print("Game over")
            print("The correct number is: ", str(computer))
            break
