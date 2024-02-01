#########
# Makes an really annoying bip sound every .5 seconds
#########

# Imports raspberry pi machine and Pin module
from machine import Pin, PWM
from time import sleep

# Creates buzzer instance at Pin 15 due to being connected into the GPIO Pin 15
# See passive-buzzer-module-bip-schema.png to visualize the Pin 15 connection and ground connection
buzzer = PWM(Pin(2))
buzzer.freq(2000)

while True:
    buzzer.duty_u16(49152) 
    sleep(0.5)
    buzzer.duty_u16(0)
    sleep(0.5)
