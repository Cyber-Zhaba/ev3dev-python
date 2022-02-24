#!/usr/bin/env python3
from ev3dev.auto import *
from PIL import Image
from time import sleep

from sub import *


def Start():
    Leds.all_off()
    Leds.set_color(Leds.LEFT, Leds.GREEN, 255)
    Leds.set_color(Leds.RIGHT, Leds.GREEN, 255)

    while True:
        if Button().any():
            break
        else:
            sleep(0.01)


def main():
    Start()

    while True:
        print(cl_1.value(), cl_2.value())
        sleep(0.5)


main()
