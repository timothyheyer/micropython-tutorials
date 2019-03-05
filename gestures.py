from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)