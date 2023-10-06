#########
# Flashes LED Raspberry PI Pico W
#########

# Imports raspberry pi machine and Pin module
from machine import Pin
from time import sleep

# Sets led as the actual LED pin module as output
led = Pin("LED", machine.Pin.OUT)

while True:
    sleep(1)
    led.off()
    sleep(1)
    led.on()