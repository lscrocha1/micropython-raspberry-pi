import socket
import network
import ntptime
from time import sleep

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('', '')

while wifi.isconnected() == False:
    print('Waiting for connection')
    sleep(1)

wifiInfo = wifi.ifconfig()
print(wifiInfo)

ntptime.host = "br.pool.ntp.org"

try:
  print("Local time before synchronization：%s" %str(time.localtime()))
  #make sure to have internet connection
  ntptime.settime()
  print("Local time after synchronization：%s" %str(time.localtime()))
except:
  print("Error syncing time")