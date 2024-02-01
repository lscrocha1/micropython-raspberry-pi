from machine import Pin, PWM
from time import sleep
from datetime import datetime, timedelta

# Define GPIO constants
BUTTON_PIN = 15
BUZZER_PIN = 2

# Define buzzer constants
BUZZER_MAX_FREQUENCY = 2000
BUZZER_MAX_PULSE = 49152
BUZZER_MIN_PULSE = 0
BUZZER_SLEEP_TIME = 0.5

# Setups Button
def setup_button() -> Pin:
    button_pin = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
    return button_pin

# Setups PWM Buzzer
def setup_buzzer() -> PWM:
    buzzer_pin = PWM(Pin(BUZZER_PIN))
    buzzer_pin.freq(BUZZER_MAX_FREQUENCY)
    return buzzer_pin

button = setup_button()
buzzer = setup_buzzer()

# one_minute_from_now = datetime.now() + timedelta(minutes=1)

# if (one_minute_from_now.hour == datetime.now().hour 
#     and one_minute_from_now.minute == datetime.now()):
    while True:
        buzzer.duty_u16(BUZZER_MAX_PULSE) 
        sleep(BUZZER_SLEEP_TIME)
        buzzer.duty_u16(BUZZER_MIN_PULSE)
        sleep(BUZZER_SLEEP_TIME)

