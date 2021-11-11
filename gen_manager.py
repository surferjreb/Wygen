from wiegand_gen import WiegandGen
from card_data import CardData


class GenManager:
    def __init__(self):
        self.card_list = CardData()

    def gen_card_bin(self, cardNumber, fac_code):

        wiegand = WiegandGen()
        card = wiegand.card_bin_gen(cardNumber, fac_code)
        self.write_to_list(card)

    def write_to_list(self, card):
        try:
            self.card_list.cards.append(card)
        except Exception:
            print('card already in list')

    def output_csv(self):
        file = open('cards.txt', 'a')
        for card in self.card_list.cards:
            file.writelines([card, '\n'])

        self.card_list.cards.clear()
        file.close()
