#########
# Shows two lines into the smal SSD1306 I2C Display
#########

from ssd1306 import SSD1306_I2C
from machine import Pin, I2C

# Check pi-ssd1306-led-screen-schema.jpeg to see
sdaPin = Pin(2)
sclPin = Pin(3)

# Needs to verify why this 400.000 is the defualt in many examples
displayFrequency = 400000

# Since SDA and SCL Pin are in GPIO2 and GPIO3
# The I2C type is 1, go into to gpio-pins.png
# And check that those pins are I2C1 type
i2cType=1

# Creates i2cbus instance
i2cBus = I2C(
    i2cType,
    sda = sdaPin,
    scl = sclPin,
    freq = displayFrequency)

# The 128 and 64 here are the heigth and width of the SSD1306 I2C
width = 128
height = 64
display=SSD1306_I2C(width, height, i2cBus)

msg = 'Hello World!'
secondMessage = 'It works!!'

# Display text in 0, 0 in X and Y respectively
display.text(msg, 0, 0)
display.text(secondMessage, 0, 16)
display.show()
# display.poweron()
# display.poweroff()
