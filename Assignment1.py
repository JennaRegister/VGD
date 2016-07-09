import random

def guessing_game(minimum, maximum):
    answer = random.randint(minimum, maximum)
    guess = None

    number_of_guesses = 0

    print("I'm thinking of a number between", minimum, "and", maximum)

    while guess != answer:
        guess = int(input("> "))
        number_of_guesses = number_of_guesses + 1

        if guess > answer:
            print("Too high!")
        elif guess < answer:
            print("Too low!")
        else:
            print("Got it! It took you", number_of_guesses, "tries")

def guessing_game_replay(minimum=1, maximum=100):

    playing = True
    while playing:
        guessing_game(minimum, maximum)

        response = input("play again? [Y/n]")
        if len(response) >= 1 and response[0].lower() == "n":
            break

    print("thanks for playing!")

guessing_game_replay()