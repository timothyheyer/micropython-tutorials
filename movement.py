from microbit import *

while True:
    reading = accelerometer.get_x()
    tilt = accelerometer.get_y()
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    elif tilt > 500:
        display.show("UP")
    elif tilt < 5:
        display.show("DOWN")
    else:
        display.show("-")