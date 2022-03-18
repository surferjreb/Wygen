from machine import Pin
import time

dz = Pin(14, Pin.OUT, Pin.PULL_UP)
d1 = Pin(15, Pin.OUT, Pin.PULL_UP)
card_read = Pin(25, Pin.OUT, Pin.PULL_DOWN)
# facility code 140
# card: 420 - 425
cards = []

def run_card(card):
    print(card)
    card_read.on()
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
    card_read.off()
    time.sleep(8)
        
def read_cards():
    with open('cards.txt', 'r') as file:
        for line in file:
            card = line.strip('\n')
            run_card(card)
        # card.strip('\n\n')
        
time.sleep(2)
while True:
        read_cards()
        
        
            


        