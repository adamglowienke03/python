import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
games = 1
user_wins = 0
computer_wins = 0
draws = 0

def blackjack():
    global games, user_wins, computer_wins, draws
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    while True:
        user_cards_score = sum(user_cards)
        computer_cards_score = sum(computer_cards)
        print(f"\nGame {games} - User wins: {user_wins}, Computer wins: {computer_wins}, Draws: {draws}")
        print(f"Your cards: {user_cards}, score: {user_cards_score}")
        print(f"Computer: [{computer_cards[0]}, ?]")

        if user_cards_score == 21:
            print("Blackjack! You win!")
            user_wins += 1
            break
        elif computer_cards_score == 21:
            print("Computer has blackjack. You lose!")
            print(f"Computer: [{computer_cards[0]}, {computer_cards[1]}]")
            computer_wins += 1
            break

        if user_cards_score > 21:
            while 11 in user_cards and sum(user_cards) > 21:
                user_cards[user_cards.index(11)] = 1
                user_cards_score = sum(user_cards)

            if user_cards_score > 21:
                print("You busted! You lose.")
                computer_wins += 1
                break
            
        user_decision = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_decision == "y":
            os.system('cls' if os.name == 'nt' else 'clear')

            user_cards.append(random.choice(cards))
            continue
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

            while computer_cards_score < 17:
                computer_cards.append(random.choice(cards))
                computer_cards_score = sum(computer_cards)

            print(f"\nFinal hands:")
            print(f"Your cards: {user_cards}, score: {user_cards_score}")
            print(f"Computer: {computer_cards}, score: {computer_cards_score}")

            if computer_cards_score > 21:
                print("Computer busts. You win!")
                user_wins += 1
            elif computer_cards_score > user_cards_score:
                print("Computer wins!")
                computer_wins += 1
            elif computer_cards_score < user_cards_score:
                print("You win!")
                user_wins += 1
            else:
                print("It's a draw!")
                draws += 1
            break

    games += 1
    again = input("\nPlay again? (y/n): ")
    if again == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        blackjack()
    else:
        print(f"\nFinal score after {games-1} games: You {user_wins} - Computer {computer_wins} - Draws {draws}")

blackjack()
