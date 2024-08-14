import sys
import time
from network import WLAN
import pop
import json
import socket


co2 = pop.CO2()
soil = pop.SoilMoisture()
light_in = pop.Light(0x5C)
tphg_in = pop.Tphg(0x76)


b1 = { "CO2":0, "SoilMoisture":0, "Light_0x5C":0, "Temperature":0, "Humidity":0}
#b = json.loads(b)
print(b1)
'''
b1.co2val = pop.CO2().read()
b1.soilval = pop.SoilMoisture().read()
b1.light_inval = light_in.read()
b1.tempin, _, b1.humiin, _ = tphg_in.read()'''

#b = '{ "co2val":0, "soilval":0, "light_inval":0, "tempin":0, "humiin":0}'
#b1 = json.loads(b)
b1['CO2'] = co2.read()
b1['SoilMoisture'] = soil.read()
b1['Light_0x5C'] = light_in.read()
b1['Temperature'], _, b1['Humidity'], _ = tphg_in.read()

print(b1)


