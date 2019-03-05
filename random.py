from microbit import *
import random

cities = ["Denver", "Aurora", "Boulder", "Vail", "Aspen", "Breckenridge", "Englewood"]

display.scroll(random.choice(cities))