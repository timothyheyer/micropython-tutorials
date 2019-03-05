from microbit import *

sleep(1200)
display.scroll(str(button_b.get_presses()-5))