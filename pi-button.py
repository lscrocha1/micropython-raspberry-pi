#########
# Configures button
#########

from machine import Pin
from time import sleep

button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    buttonState = button.value()
    print(buttonState)
    sleep(.21)