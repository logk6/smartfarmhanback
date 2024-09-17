

# Import socket module
import socket
import json
import pyodbc


# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(40.0) 
print(s)
# Define the port on which you want to connect
port = 40674

try:
    # Attempt to connect to a server"172.31.99.116
    s.connect(("172.31.98.24", port))
    #s.send(b'{ "mess":"ledoff", "rgb1":255, "rgb2":0, "rgb3":0}')
    s.send(b'{ "mess":"fanheatoff"}') 
    a = s.recv(1024).decode('utf8')
    print(a)

    a = s.recv(1024).decode('utf8')
    print(a)
except socket.timeout:
    print("Connection timed out")
finally:
    s.close()



#
# receive data from the server
#



''''''


""" 
a = '{"mess":"measre", "rgb1":255, "rgb2":0, "rgb3":0}'
a0 = json.loads(a)

print(a0['rgb1'])
print(type(a0['rgb1']))
"""














