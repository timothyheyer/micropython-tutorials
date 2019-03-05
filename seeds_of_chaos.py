from microbit import *
import random

random.seed(50000)
while True:
    if button_a.was_pressed():
        display.show(str(random.randint(1, 6)))
    if button_b.was_pressed():
        display.show(str(random.randint(7, 9)))