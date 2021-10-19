from machine import Pin
import time

dz = Pin(14, Pin.OUT, Pin.PULL_UP)
d1 = Pin(15, Pin.OUT, Pin.PULL_UP)
card_read = Pin(25, Pin.OUT, Pin.PULL_DOWN)
# facility code 140
# card: 420 - 425
cards = []

def read_card(card):
    for bit in card:
        if bit == '0':
            dz.off()
            time.sleep_us(40)
            dz.on()
        if bit == '1':
            d1.off()
            time.sleep_us(40)
            d1.on()
        time.sleep_ms(2)
        
def add_cards():
    file = open('cards.txt', 'r')
    cards = file.readlines().split('\n')
        
while True:
    add_cards()
    for card in cards:
        card_read.on()
        read_card(card)
        card_read.off()
        time.sleep(10)
        
