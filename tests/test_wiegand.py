from wiegand_gen import WiegandGen
import pytest


@pytest.fixture
def wygen():
    return WiegandGen()


@pytest.fixture
def card():
    fac_code = 40
    card_number = 416
    card_26bit = '00010100000000001101000000'
    return (fac_code, card_number, card_26bit)


def test_card_to_binary(wygen, card):
    card_bin = wygen.cNumToBin(card[1])
    card_binary_string = bin(card[1]).strip('0b')
    assert len(card_bin) == 16
    assert isinstance(card_bin, str)
    assert card_bin.strip('0') == card_binary_string


def test_fac_to_binary(wygen, card):
    fac_bin = wygen.facToBin(card[0])
    fac_code_bin = bin(card[0]).strip('0b')
    assert len(fac_bin) == 8
    assert isinstance(fac_bin, str)
    assert fac_bin.strip('0') == fac_code_bin


def test_even_parity(wygen, card):
    fac_bin = wygen.facToBin(card[0])
    fac_w_parity = wygen.add_even_parity(fac_bin)
    assert fac_w_parity == card[2][:9]


def test_odd_parity(wygen, card):
    code_bin = wygen.cNumToBin(card[1])
    card_w_parity = wygen.add_odd_parity(code_bin)
    assert card_w_parity[16] == '0'


def test_card_bin_gen(wygen, card):
    card_bin = wygen.card_bin_gen(card[0], card[1])
    assert len(card_bin) == len(card[2])
    assert card_bin == card[2]
