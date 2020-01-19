#!/usr/bin/env python3
# Output the value for the buttons.
# The library used py-tm1638 (https://github.com/johnblackmore/py-tm1638)

# TM1638

import TM1638
import time

# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 5V and ground.

DIO = 17
CLK = 21
STB = 22

display = TM1638.TM1638(DIO, CLK, STB)

display.enable(1)
display.set_led(0, True)

count = 0
active = True
while active == True:
    keys = display.get_buttons()
    display.set_text(str(keys))
    #time.sleep(0.02)
    print(str(keys))
    if keys == 128:
        active = False

