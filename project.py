import random
from ASCII_Art import logo
print(logo)
# Generating a random number to guess.
def random_number():
    random_number = random.randint(1,100)
    return random_number
# Creating a function to choose difficulty easy or hard
def difficulty():
    difficulty = input("Choose a difficulty level. 'easy' or 'hard' : ").lower()
    if difficulty == "easy":
        chances = 10
    elif difficulty == "hard":
        chances = 5
# Game.
def game(number):
    random_number()
    difficulty()
    for i in range(difficulty):
        if chances != 0:
            if number == random_number:
                print("You guessed right")
                break
            else:
                guess_number()
                


# Creating a function to give output if the number is higher or lower to the number entered.
def guess_number():
    random_number()
    difficulty()

    if number > random_number:
        print("You guessed too high.")
        chances -= 1
        print(f"You guessed wrong. You have {chances} chances left.")
    elif number < random_number:
        print("You guessed too low.")
        chances -= 1
        print(f"You guessed wrong. You have {chances} chances left.")

number = int(input("Guess the number"))
game(number)