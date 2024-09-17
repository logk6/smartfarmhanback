import sys
import time
from network import WLAN
import pop
import json


SSID = "ICTLab Guests"; PASSWORD = "guestsss"
#SSID = "USTH_Student"; PASSWORD = "usth2021!"

print("Run")
wlan = WLAN(mode=WLAN.STA)
wlan.connect(SSID, auth=(WLAN.WPA2, PASSWORD))
while not wlan.isconnected():
    wlan.connect(SSID, auth=(WLAN.WPA2, PASSWORD))
    time.sleep(1)
    print("Connecting to IoT device...")

import socket
""""""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
port = 40674
s.connect(("172.31.98.6", port))
print(s.recv(1024))


co2val = pop.CO2().read()
soilval = pop.SoilMoisture().read()
light_inval = pop.Light(0x5C).read()
light_outval = pop.Light(0x23).read()

a0 = '{ "CO2": 0, "SoilMois": 0, "LightIn": 0, "LightOut": 0}'
a1 = json.loads(a0)
a1['CO2'] = co2val; a1['SoilMois'] = soilval; a1['LightIn'] = light_inval; a1['LightOut'] = light_outval
a = json.dumps(a1).encode('utf-8')

s.send(a)
s.close()

"""
from pop import Fan
fan = Fan()

fan.on()
time.sleep(3)
fan.off()
"""



