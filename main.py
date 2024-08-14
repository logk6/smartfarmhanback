import sys
import time
from network import WLAN
import pop
import json
import socket

SSID = "ICTLab Guests"; PASSWORD = "guestsss"
#SSID = "USTH_Student"; PASSWORD = "usth2021!"
#SSID = "iPhone"; PASSWORD = "12345678"
#SSID = "osquizzz"; PASSWORD = "osquizzz"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 



fan = pop.Fan()
rgb = pop.RgbLedBar()
window = pop.Window()
textlcd = pop.Textlcd()

co2 = pop.CO2()
soil = pop.SoilMoisture()
light_in = pop.Light(0x5C)
tphg_in = pop.Tphg(0x76)


print("Run")

rgb.on()
rgb.setColor([255, 255, 255])
time.sleep(1)
rgb.off()

wlan = WLAN(mode=WLAN.STA)
wlan.connect(SSID, auth=(WLAN.WPA2, PASSWORD))

#rgb.setColor([255, 0, 0])                
''''''
connect_cnt = 0
while not wlan.isconnected():
    wlan.connect(SSID, auth=(WLAN.WPA2, PASSWORD))
    time.sleep(0.5)
    print("Connecting to IoT device... ", connect_cnt)
    connect_cnt = connect_cnt + 1

#textlcd.print(wlan.status())

print('Connected.')
my_ip = str(wlan.ifconfig()[0])
textlcd.print(my_ip)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

print ("Socket successfully created")
port = 40674
#s.bind(('172.31.98.185', port))
s.bind(('0.0.0.0', port))
print ("socket binded to %s" %(port))

s.listen(5)  
print ("socket is listening")


'''''' 
b ='{ "co2val":0, "soilval":0, "light_inval":0, "tempin":0, "humiin":0}'

while True:
    c, addr = s.accept()
    print ('Got connection from', addr)
    
    a = c.recv(1024).decode('utf8')
    a0 = json.loads(a)
    mess = a0['mess']

    print(mess)
    if(mess == "off"):
        break
    elif(mess == "fanon"):
        fan.on()
    elif(mess == "fanoff"):
        fan.off()
    elif(mess == "windopn"):
        window.open()
    elif(mess == "windclos"):
        window.close()
    elif(mess == "ledon"):
        rgb.setColor([a0['rgb1'], a0['rgb2'], a0['rgb3']])
        rgb.on()
    elif(mess == "ledoff"):
        rgb.on()
        rgb.off()
    elif(mess == "measre"):
        '''
        co2val = co2.read()
        soilval = soil.read()
        light_inval = light_in.read()
        tempin, _, humiin, _ = tphg_in.read()'''
        
        #b = '{ "co2val":0, "soilval":0, "light_inval":0, "tempin":0, "humiin":0}'
        #b1 = json.loads(b)
        
        b1 = { "CO2":0, "SoilMoisture":0, "Light_0x5C":0, "Temperature":0, "Humidity":0}
        b1['CO2'] = co2.read()
        b1['SoilMoisture'] = soil.read()
        b1['Light_0x5C'] = light_in.read()
        b1['Temperature'], _, b1['Humidity'], _ = tphg_in.read()
        
        b = json.dumps(b1)
        res = b.encode('utf-8')
        c.send(res)
        
        
    str = "done"
    a = str.encode('utf-8')
    c.send(a)
    c.close()

