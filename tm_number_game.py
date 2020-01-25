#!/usr/bin/env python3
# A game using the LED&KEY board that has 8 LEDs, 8 7-Seg display and 8 buttons
# The goal of the game is to press the buttom related to the largest number in the display
# The library used py-tm1638 (https://github.com/johnblackmore/py-tm1638)
# Importand to note that the library uses a string to set the display
# While for setting the individual digits we're using a Python list so we can get at each digit
# Means to setup the 8 digits we use a list and then have to turn it into a string for the library 
# To convert from list to string you use the join command


# TM1638 playground
# Import all the needed libraries
import TM1638 #board
import time # sleep
import random # create random number
import math # power

# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 3.3V and ground.
DIO = 17
CLK = 21
STB = 22

# This sets the number of puzzles to solve
gamelength=5

# Initialize the board
display = TM1638.TM1638(DIO, CLK, STB)
display.enable(1)

# Display how many to find
display.set_text("find "+str(gamelength))
time.sleep(3)

# Get the starting time
starttime = time.time()

# Main looo for the lenght of the game
for x in range(gamelength):

# Get something setup for the start
        largest = 0
        number=list("00000000")
        biggest=random.randint(6,7)

# Pick 8 random numbers on the display
        for x in range(8):
            digit = random.randint(0, biggest)
            number[x] = str(digit)

# If the number is a largest number then record the location so it can be changed later
            if digit > largest:
                    largest = digit

# Add 1 to largest to make it the largest number (but only one bigger than the others
        largest+=1
        largest=str(largest)

# Pick a random number to change
        location = random.randint(0,7)

# Replace the existing number at location with the new largest number
        number[location] = largest

# Convert the list to a string using the join command
        number="".join(number)
        print(number)

# Display the 8 digits on the 7 segment
        display.set_text(number)

# Check if the correct key is pressed       

# The display.get_buttons() returns a binary number for all the 8 buttons
# From left to right they are 1, 2, 4, 8, 16, 32, 64, 128
# If you have learned about powers then these are all 2 to the power of 0,1,2,3,4,5,6,7 
# As in 2 to the power of 0 is 1
# Or    2 to the power of 7 is 128
# We know the location of our biggest digit as we set it we know the result we want

        result = pow(2,(location))
        correctkey = False
        keys = display.get_buttons()
        while correctkey==False:
            keys = display.get_buttons()
            if result==keys:
                correctkey = True
                print("keys: "+str(keys))
                print("result: "+str(result))

# Get the total time 
totaltime=time.time()-starttime

# By converting to an integer after multiplying by 100 
# And then dividing by 100 it rounds to 2 decimal places.
timing = "t "+str(int(totaltime*100)/100)

# Print the score
print(timing)
display.set_text(timing)
