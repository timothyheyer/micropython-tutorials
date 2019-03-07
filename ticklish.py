from microbit import *

while True:
    if pin1.is_touched():
        display.show(Image.MUSIC_QUAVER)
    else:
        display.show(Image.ASLEEP)