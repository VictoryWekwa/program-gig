from random import randint
game_level = input(""" Enter a level to start the game. Levels available are Easy, Medium or Hard:  """)

# Create a loop for the easy level
guess_limit = 6
guess_number = 0
guess_left = 6
secret_number = 5
while game_level == "easy":
    try:
        guess = int(input("Enter a number between 1 to 10: "))
        guess_number += 1
        guess_left -= 1
        print("You have", guess_left, "remaining from your guesses")
        if guess == secret_number:
            print("Congratulations, You got it right!")
            print("You used", guess_number, "from your available guesses")
            break
        else:
            print("You got it wrong!")
        if guess_number == guess_limit:
            print("Game over, try again!")
            print("The correct answer is", secret_number)
            break
    except ValueError:
        print("You entered an invalid command")

# Creating a loop for medium level
guess_limit = 4
guess_number = 0
guess_left = 4
secret_number = randint(1, 20)
while game_level == "medium":
    try:
        guess = int(input("Enter a number between 1 to 20: "))
        guess_number += 1
        guess_left -= 1
        print("You have", guess_left, "remaining from your guesses")
        if guess == secret_number:
            print("Wow!, You got it right")
            print("You used", guess_number, "from your available guesses")
            break
        else:
            print("You got it wrong!")
        if guess_number == guess_limit:
            print("Game over, try again!")
            print("The correct answer is", secret_number)
            break
    except ValueError:
        print("You have entered an invalid command")
# Create a loop for the hard Level
guess_limit = 3
guess_number = 0
guess_left = 3
secret_number = randint(1, 50)

while game_level == "hard":
    try:
        guess = int(input("Enter a number between 1 to 50: "))
        guess_number += 1
        guess_left -= 1
        print("You have", guess_left, "remaining from your guesses")
        if guess == secret_number:
            print("Awesome! You got it right")
            print("You used", guess_number, "from your available guesses")
            break
        else:
            print("You got it wrong!")
        if guess_number == guess_limit:
            print("Game over, try again!")
            print("The correct answer is", secret_number)
            break
    except ValueError:
        print("You have entered an invalid command")
