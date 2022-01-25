
class WiegandGen:
    def __init__(self):
        self._card = None

    def decimalToBinary(self, num):
        return bin(num).replace("0b", "")

    def cNumToBin(self, card):
        card = self.decimalToBinary(card)
        card_index = 16

        while len(card) < card_index:
            card = '0' + card
        
        return card
    
    def add_odd_parity(self, card):
        count = 0
    
        for i in card:
            if i == '1':
                count += 1

        if count % 2 != 0:
            return card + '0'

        return card + '1'

    def facToBin(self, fac_code):
        fac_bin = self.decimalToBinary(fac_code)
        fac_index = 8

        while len(fac_bin) < fac_index:
            fac_bin = '0' + fac_bin

        return fac_bin
        
    def add_even_parity(self, fac):
        count = 0

        for i in fac:
            if i == '1':
                count += 1

        if count % 2 == 0:
            return '0' + fac

        return '1' + fac

    def card_bin_gen(self, card_number, fac_code):
        fac_bin = self.facToBin(fac_code)
        fac_bin_code = self.add_even_parity(fac_bin)
        c_bin = self.cNumToBin(card_number)
        c_bin_code = self.add_odd_parity(c_bin)

        self._card = fac_bin + c_bin
        return self._card
