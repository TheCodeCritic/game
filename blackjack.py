# blackjack - get as close to 21 without going over
from random import randint

cards = 0

currentCard = randint(1,8)
cards = cards + currentCard
print(f"Your card is {str(currentCard)}")

while cards != 21 or cards < 21:
    # main game loop
    newCard = randint(1, 10)
    choice = input("Hit or fold: ").upper()

    if choice == "HIT":
        if newCard + cards > 21:
            print(f"You went bust!")
            print(f"You had {str(cards)}")
            break

        cards = cards + newCard
        print(f"Your card is {str(newCard)}")
    elif choice == "FOLD":
        continue

if cards == 21:
    print("BLACKJACK!!")
