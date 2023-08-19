'''
----------------- DISCLAIMER ------------------
As a Muslim, I don't support gambling or Casino. This is a program just for practice purposes.
I personally do not encourage people to go to casinos. I think it's a trap.

'''

import random

# List of possible card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Initialize user and dealer hands with 2 random cards each
user_hand = random.choices(cards, k=2)
dealer_hand = random.choices(cards, k=2)

# Calculate the initial sums of user and dealer hands
user_sum = sum(user_hand)
dealer_sum = sum(dealer_hand)

# Check if dealer has an ace (11). If total sum exceeds 21, treat it as 1.
if 11 in dealer_hand:
    if dealer_sum > 21:
        get_index = dealer_hand.index(11)
        dealer_hand[get_index] = 1

# Dealer's turn: draw cards until sum is 17 or higher
while True:
    if dealer_sum < 17:
        dealer_hand.append(random.choice(cards))
        dealer_sum = sum(dealer_hand)
    else:
        break

# Player's turn
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

# Determine the game result
if dealer_sum > 21:
    print('You win!')
    # Display cards in user's and dealer's hands (optional)
    print(f"Your hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")
elif dealer_sum > user_sum:
    print("Bust! You lose.")
    # Display cards in user's and dealer's hands (optional)
    print(f"Your hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")
elif dealer_sum == user_sum:
    print("Draw.")
    # Display cards in user's and dealer's hands (optional)
    print(f"Your hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")
else:
    print('You win!')
    # Display cards in user's and dealer's hands (optional)
    print(f"Your hand: {user_hand}")
    print(f"Dealer hand: {dealer_hand}")
