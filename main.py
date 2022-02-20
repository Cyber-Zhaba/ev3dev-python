#!/usr/bin/env python3
from ev3dev.auto import *
from PIL import Image
from time import sleep


def Start():
    lcd = Screen()
    start_img = Image.open('pics/pentium.jpg')
    lcd.image.paste(start_img, (-10, -10))
    lcd.update()

    Sound().beep()

    while True:
        if Button().any():
            break
        else:
            sleep(0.01)


def main():
    Start()

    Sound.beep()
    while True:
        pass


main()
