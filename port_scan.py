import socket

#Port that you wanna scan here
ports = [21, 23, 80, 443, 8080]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex(("URL OR IP HERE", port))
     
    #If any port is open, it'll be printed :)
    if code == 0:
        print(port)
