class Deck():
    def __init__(self, alphabet=None):
        self.card_obj_list = []
        self.target_list = ['Mana Crypt', 'Grim Monolith', 'Sol Ring'] # return value of moxfield_get_decklist

    def make_cards_obj(self, lst):
        if len(self.target_list) > 0:
            self.card_obj_list.append(Card(self.target_list[-1]))
            self.target_list.pop()
            self.make_cards_obj(self.target_list)
        return self.target_list

class Card():
    def __init__(self, card_name):
        self.card_name = card_name



def tri_recursion2(target_list):
    if len(target_list) > 0:
        print(target_list[-1])
        target_list.pop()
        tri_recursion2(target_list)
    return target_list

# alphabet = ['Mana Crypt', 'Grim Monolith', 'Sol Ring']
practice = Deck()
practice.make_cards_obj(practice.target_list)
for i in practice.card_obj_list:
    print(f"Card Name: {i.card_name}")
    print(type(i))