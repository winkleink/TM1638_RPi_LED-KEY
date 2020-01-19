#!/usr/bin/env python3
# A program using the LED&KEY board that has 8 LEDs, 8 7-Seg display and 8 buttons
# Create the sequenece of LEDs going back and forth like Knight Rider to Battlestar Galactica Cylons
# The library used py-tm1638 (https://github.com/johnblackmore/py-tm1638)

# TM1638 playground

import TM1638
import time

# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 5V and ground.

DIO = 17
CLK = 21
STB = 22

pause = 0.01

display = TM1638.TM1638(DIO, CLK, STB)

display.enable(1)
display.set_led(0, True)

for x in range(5):
    for i in range(7):
        display.set_led(i,True)
        time.sleep(pause)
        display.set_led(i,False)
        time.sleep(pause)

    for i in range (7,0,-1):
        display.set_led(i,True)
        time.sleep(pause)
        display.set_led(i,False)
        time.sleep(pause)
