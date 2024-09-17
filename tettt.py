import socket
import pyodbc
import json


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")
port = 40674
#10.10.14.11
s.bind(('0.0.0.0', port))

print ("socket binded to %s" %(port))

s.listen(5)    
print ("socket is listening")

while True:
  
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    #mess = c.recv(1024).decode('utf8')
    #print(mess)
    #if(mess == "off"):
    #    break
    

    a0 = '{\h"SoilMoisture\": 2519, \"Temperature\": 28.16, \"CO2\": 997, \"Humidity\": 53.38, \"Light_0x5C\": 18}' #'{ "CO2":1, "SoilMoisture":0, "Light_0x5C":0}'
    a1 = json.loads(a0)
    a = json.dumps(a1).encode('utf-8')
 
    c.send(a)
    
    #a0 = c.recv(1024).decode('utf-8')
    #a = json.loads(a0)
    #print(type(a))
    #print(a1)

    
    # Close the connection with the client
    c.close()
    





