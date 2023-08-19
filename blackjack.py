import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = random.choices(cards, k=2)
dealer_hand = random.choices(cards, k=2)

user_sum = sum(user_hand)
dealer_sum = sum(dealer_hand)

if 11 in dealer_hand:
    if dealer_sum > 21:
        get_index = dealer_hand.index(11)
        dealer_hand[get_index] = 1

while True:
    if dealer_sum < 17:
        dealer_hand.append(random.choice(cards))
        dealer_sum = sum(dealer_hand)
    else:
        break

while True:
    print(f"User hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand[0]}")
    user_choice = input("hit or stand? (type h or s): ")
    if user_choice.upper() == 'H':
        user_hand.append(random.choice(cards))
        user_sum = sum(user_hand)
        if user_sum > 21:
            print(f"User hand: {user_hand}")
            print("Bust! You lose.")
            break
    else:
        break


if dealer_sum > 21:
    print('You win!')
    # showing the cards in user's hand and dealer's hand. Showing is optional
    print(f"Your hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")
elif dealer_sum > user_sum:
    print("Bust! You lose.")
    # showing the cards in user's hand and dealer's hand. Showing is optional
    print(f"Your hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")
elif dealer_sum == user_sum:
    print("Draw.")
    # showing the cards in user's hand and dealer's hand. Showing is optional
    print(f"Your hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")
else:
    print('You win!')
    # showing the cards in user's hand and dealer's hand. Showing is optional
    print(f"Your hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")
