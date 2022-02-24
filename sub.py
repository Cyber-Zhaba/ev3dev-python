#!/usr/bin/env python3
from ev3dev.auto import *
from PIL import Image
from time import sleep


cl_1 = ColorSensor('in1')
cl_1.mode = 'COL-REFLECT'

cl_2 = ColorSensor('in2')
cl_2.mode = 'COL-REFLECT'
