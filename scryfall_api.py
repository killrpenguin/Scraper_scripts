import requests
from bs4 import BeautifulSoup
import re
import json

link = "https://api.scryfall.com/cards/named?exact=" + "Mana Crypt"
page = requests.get(link)
soup = BeautifulSoup(page.text, "html.parser")
card_dict = json.loads(soup.text)
name = card_dict['name']
print(name)