import random 
import json

with open('E:\Python\Python-PGR107\Selvstudium_Ole\cards.json', 'r') as file:
    cards = json.load(file)


def rand_card_func():
    if not cards['cards']:
        print("There are no more cards in the deck")
        return
    random_id = random.randint(1,52)
    for card in cards['cards'] :
        if card['id'] == random_id:
            print("The card is:",card['name'],)
            cards['cards'].remove(card)
            break


while True :
    userInput = input("Enter 'Q' to quit the game or 'N' for next card: ")
    if userInput == 'Q' :
        print("Goodbye!")
        print("-" * 20)
        break
    elif userInput == 'N' :
        rand_card_func() 
        print("-" * 20)
        if not cards['cards']:
            break
    else :
        print("You entered an invalid input. Try again ->  \n" )
        print("-" * 20)
        