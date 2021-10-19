
class WiegandGen:
    def __init__(self, cardNumber, fac_code):
        self.cardNumber = cardNumber
        self.fac_code = fac_code
        self.card = None

    def decimalToBinary(self, num):
        return bin(num).replace("0b", "")

    def cNumTo26Bin(self, card):
        card = self.decimalToBinary(card)
        card_index = 16

        while len(card) < card_index:
            card = '0' + card
        
        card = self.add_odd_parity(card)
        return card
    
    def add_odd_parity(self, card):
        count = 0
    
        for i in card:
            if i == '1':
                count += 1

        if count % 2 != 0:
            return card + '1'

        return card + '0'

    def facTo26Bin(self, fac_code):
        fac_bin = self.decimalToBinary(fac_code)
        fac_index = 8

        while len(fac_bin) < fac_index:
            fac_bin = '0' + fac_bin

        fac_bin = self.add_even_parity(fac_bin)
        return fac_bin
        
    def add_even_parity(self, fac):
        count = 0

        for i in fac:
            if i == '1':
                count += 1

        if count % 2 == 0:
            return '1' + fac

        return '0' + fac

    def card_bin_gen(self):
        fac_bin = self.facTo26Bin(self.fac_code)
        c_bin = self.cNumTo26Bin(self.cardNumber)
        self.card = fac_bin + c_bin
