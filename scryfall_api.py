import requests
from bs4 import BeautifulSoup
import re
import json

link = "https://api.scryfall.com/cards/named?fuzzy=" + "Valki, God of Lies // Tibalt, Cosmic Impostor"
page = requests.get(link)
soup = BeautifulSoup(page.text, "html.parser")
card_dict = json.loads(soup.text)
name = card_dict['name']
print(card_dict['layout'])
print(f"Front: {card_dict['card_faces'][0]['name']} \nBack: {card_dict['card_faces'][1]['name']}")
if card_dict['layout'] == 'modal_dfc':
    print(type(name))
