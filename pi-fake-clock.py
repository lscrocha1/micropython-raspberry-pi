from machine import Pin, PWM
from time import sleep
from datetime import datetime, timedelta, timezone
from network import WLAN
import ntptime
import network
import time

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

# Setups WiFi
def setup_wifi() -> WLAN:
    wifi_lan = network.WLAN(network.STA_IF)
    wifi_lan.active(True)
    wifi_lan.connect('', '')
    while wifi_lan.isconnected() == False:
        print('Waiting for WiFi connection...')
        sleep(1)
    return wifi_lan

# Sets current date and time from br ntp
def set_current_date_time():
    ntptime.host = "br.pool.ntp.org"
    ntptime.settime()
    current_time = time.localtime();
    return datetime(
         year = current_time[0], 
         month = current_time[1],
         day = current_time[2], 
         hour = current_time[3],
         minute = current_time[4],
         second = current_time[5],
         microsecond= current_time[6],
         tzinfo=timezone(timedelta(hours=0)))

def should_start_bip(date_time_alarm) -> bool:
     current_time = time.localtime()

     if(date_time_alarm.hour == current_time[3]
        and date_time_alarm.minute == current_time[4]):
        return True
     
     return False

button = setup_button()
buzzer = setup_buzzer()
wifi = setup_wifi()
date_time_now = set_current_date_time()

one_minute_from_now = date_time_now + timedelta(minutes=1)

while True:
    if (should_start_bip(one_minute_from_now)):
        buzzer.duty_u16(BUZZER_MAX_PULSE) 
        sleep(BUZZER_SLEEP_TIME)
        buzzer.duty_u16(BUZZER_MIN_PULSE)
        sleep(BUZZER_SLEEP_TIME)

