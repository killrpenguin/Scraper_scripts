from dataclasses import dataclass, field
from typing import Dict, List
import time
import json
import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup


class Deck():
    def __init__(self):
        self.card_obj_list = []
        self.deck_list = ['Mana Crypt', 'Grim Monolith', 'Sol Ring', 'catch // release']

    def make_cards_obj(self, *args) -> list:
        if (len(self.deck_list) > 0) and (type(self.deck_list[-1]) is str):
            self.card_obj_list.append(Card(self.deck_list[-1]))
            self.deck_list.pop()
            self.make_cards_obj(self.deck_list)
        return self.deck_list

class Card(Deck):
    def __init__(self, card_name):
        super().__init__()
        self.card_name = card_name
        self.card_dict = {}
        self.card_layout = self.card_dict['layout']
        self.faces = []
        self.legal_status = self.card_dict['legalities']['commander']

    def display_card(self):
        print(f"Card Name: {self.card_name}\n"
              f"Layout: {self.card_layout}")
        for face in self.faces:
            print(f"\ncmc: {face.cmc}, mc: {face.mana_cost}, type: {face.card_type}, colors: {face.color_ident}")


    VALID_STATUSES = [200, 301, 302, 307, 404]
    api_link = "https://api.scryfall.com/cards/named?fuzzy="
    deck_list = ['Mana Crypt', "Mox Amber", "Mox Opal", "Sol Ring"]

    async def req_json(self, session, api_link):
        VALID_STATUSES = [200, 301, 302, 307, 404]
        try:
            async with session.get(api_link, timeout=500) as resp:
                await resp.json()
                # asyncio.sleep is used to restrict requests to < 10 per sec, per skcryfall api guidelines.
                await asyncio.sleep(.12)
                if resp.status in VALID_STATUSES:
                    async with session.get(resp.url, timeout=500) as json_resp:
                        self.card_dict =json.loads(await json_resp.read())
                        self.make_faces(self.card_dict)
        except Exception as e:
            print(f"Exception: {e}")
        return await self.card_dict


    async def main(self):
        api_link = "https://api.scryfall.com/cards/named?fuzzy="
        tcp_connection = aiohttp.TCPConnector(limit=250)
        header = {"Authorization": "Basic bG9naW46cGFzcw=="}
        async with aiohttp.ClientSession(connector=tcp_connection, headers=header, trust_env=True) as session:
            try:
                tasks = [asyncio.create_task(self.req_json(session, api_link=api_link + card)) for card in self.deck_list]
                for task in tasks:
                    await task
            except Exception as e:
                print(f"Exception: {e}")
            await asyncio.sleep(0)


    def make_faces(self, card) -> list:
        faces = []
        try:
            for side in range(len(card['card_faces'])):
                faces.append(Face(face_name=card['card_faces'][side]['name'],
                                  cmc=card['cmc'], mana_cost=card['card_faces'][side]['mana_cost'],
                                  card_type=card['card_faces'][side]['type_line'],
                                  card_text=card['card_faces'][side]['oracle_text'],
                                  color_ident=card['color_identity']))
        except KeyError:
            faces.append(Face(face_name=card['name'], cmc=card['cmc'], mana_cost=card['mana_cost'],
                              card_type=card['type_line'], card_text=card['oracle_text'],
                              color_ident=card['color_identity']
                              ))
        return faces


@dataclass
class Face(Deck):
    face_name: str = field(default=str)
    cmc: float = field(default=float)
    mana_cost: str = field(default=str)
    card_type: str = field(default=str)
    card_text: List = field(default=list)
    color_ident: str = field(default=str)


practice = Deck()
practice.make_cards_obj(practice.deck_list)
for i in practice.card_obj_list:
    print(i.faces)