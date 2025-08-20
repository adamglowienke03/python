import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    user_cards = []
    computer_cards = []
    is_playing = True
    user_cards.extend([random.choice(cards), random.choice(cards)])
    computer_cards.extend([random.choice(cards), random.choice(cards)])


    while is_playing:
        user_cards_score = sum(user_cards)
        computer_cards_score = sum(computer_cards)
        print(f"Your cards: {user_cards}, score: {user_cards_score}\nComputer: {computer_cards}, score: {computer_cards_score}")
        if user_cards_score == 21:
            print("User has blackjack. You won!")
            break
        elif computer_cards_score == 21:
            print("Computer has blackjack. You lose!")
            break
        else:
            if user_cards_score > 21:
                if 11 in user_cards:
                    user_cards[user_cards.index(11)] = 1
                    user_cards_score = sum(user_cards)

                if user_cards_score > 21:
                    print("You lose!")
                    break
            else:
                user_decision = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_decision == "y":
                    user_cards.append(random.choice(cards))
                    continue
                else:
                    break


        
blackjack()




