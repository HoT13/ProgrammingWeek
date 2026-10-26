import random

def guess_game():
    x = random.randint(1, 100)
    print("Guess a number between 1-100 (or 0 to quit):")
    while True:
        guess = int(input("Your guess: "))
        if guess == 0:
            print(f"Game over! The number was {x}")
            break
        elif guess == x:
            print("Correct! You win!")
            break
        elif guess > x:
            print("Too high!")
        else:
            print("Too low!")

guess_game()