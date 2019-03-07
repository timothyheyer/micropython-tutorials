from microbit import *
import music

while True:
    music.pitch(abs(accelerometer.get_y()), 10)