from microbit import *

box1 = Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

box2 = Image("88888:"
             "88888:"
             "88888:"
             "88888:"
             "88888")

box3 = Image("77777:"
             "77777:"
             "77777:"
             "77777:"
             "77777")

box4 = Image("66666:"
             "66666:"
             "66666:"
             "66666:"
             "66666")

box5 = Image("55555:"
             "55555:"
             "55555:"
             "55555:"
             "55555")

box6 = Image("44444:"
             "44444:"
             "44444:"
             "44444:"
             "44444")

box7 = Image("33333:"
             "33333:"
             "33333:"
             "33333:"
             "33333")

box8 = Image("22222:"
             "22222:"
             "22222:"
             "22222:"
             "22222")

glow_box = [box1, box2, box3, box4, box5, box6, box7, box8, box7, box6, box5, box4, box3, box2, box1]
display.show(glow_box, loop=True, delay=300)