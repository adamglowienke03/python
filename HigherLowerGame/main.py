from game_data import data
import random

def new_game():
    decision = input("Do you want to play a new game? (y/n): ").lower()
    if decision == "y":
        game()
    else:
        print("Thanks for playing!")
        return False

def game():
    is_playing = True
    score = 0
    while is_playing:
        rand_a = random.randint(0, len(data)-1)
        rand_b = random.randint(0, len(data)-1)

        print(f"Compare A: {data[rand_a]["name"]}, {data[rand_a]["description"]}, from {data[rand_a]["country"]}")
        print("VS")
        print(f"Compare B: {data[rand_b]["name"]}, {data[rand_b]["description"]}, from {data[rand_b]["country"]}")

        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if player_choice == "a":
            if data[rand_a]["follower_count"] > data[rand_b]["follower_count"]:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                is_playing = new_game()
        elif player_choice == "b":
            if data[rand_b]["follower_count"] > data[rand_a]["follower_count"]:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                is_playing = new_game()
        else:
            print("Invalid input. Please type 'A' or 'B'.")

game()