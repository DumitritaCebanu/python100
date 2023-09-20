import random

print("Welcome to the Number Guessing game")
print("i'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty: 'easy' or 'hard': ")
random_number = random.randint(1, 100)
# print(random_number)


def play_mode(attempts):
    while attempts != 0:
        guess_number = int(input("Make a guess: "))
        if guess_number < random_number:
            print("too low, guess again")
            print(f"You have {attempts - 1} to  guess the number")
        if guess_number > random_number:
            print("too high, guess again")
            print(f"You have {attempts - 1} attempts to  guess the number")
        if guess_number == random_number:
            print(f"the {guess_number} is the number I thought of ")
            break
        attempts -= 1
        if attempts == 0:
            print(f"You lost - the number was  {random_number}")
            break


if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number")
    play_mode(10)
if difficulty == "hard":
    print("You have 5 attempts remaining to guess the number")
    play_mode(5)
