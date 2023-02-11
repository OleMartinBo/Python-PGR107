import random 
import json

with open('E:\Python\Python-PGR107\Selvstudium_Ole\cards.json', 'r') as file:
    cards = json.load(file)


suits = ["clubs ", "diamonds ", "hearts ", "spades "]
index_suits = random.randint(0, 3)
random_suit = suits[index_suits]


random_id = random.randint(1,13)

for card in cards['cards'] :
    if card['id'] == random_id:
        print(card['name'], random_suit)
        break