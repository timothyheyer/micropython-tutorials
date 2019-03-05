from microbit import *
import random

answer = random.randrange(5) + random.random()
display.scroll(str(answer))