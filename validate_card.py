class ValidateCard:
    def __init__(self):
        self.MAX_FAC_CODE = 255
        self.MAX_CARD_NUM = 65535
        self.BIN_LENGTH = 26

    def check_fac_code(self, fac_code):
        if self.check_not_zero(fac_code):
            if fac_code <= self.MAX_FAC_CODE:
                return True

            return False

    def check_card_number(self, cardNumber):
        if self.check_not_zero(cardNumber):
            if cardNumber <= self.MAX_CARD_NUM:
                return True

            return False

    def check_not_zero(self, num):
        if num > 0:
            return True

        return False

    def validate_binary(self, bin_card):
        if len(bin_card) == self.BIN_LENGTH:
            return True

        return False
