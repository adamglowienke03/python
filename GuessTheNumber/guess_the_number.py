import random

print("Welcome to the game, guess the number!\nI will choose a number from 1 to 100")
random_number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type ('easy' or 'hard'): ")

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

while True:
    if attempts == 1:
        print(f"You have {attempts} attempt remaining")
    else:
        print(f"You have {attempts} attempts remaining")

    guess = int(input("Guess a number: "))
    if guess == random_number:
        print(f"Congratulations!!! You guessed the right number")
        break
    elif guess < random_number:
        print("Your guess is too low")
        attempts -= 1
    elif guess > random_number:
        print("Your guess is too high")
        attempts -= 1

    if attempts == 0:
        print(f"You lose, the number was {random_number}")
        break
