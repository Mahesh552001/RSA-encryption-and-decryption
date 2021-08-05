import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

#client
import socket  
s = socket.socket()   
host = socket.gethostname()  
port = 9999    
s.connect((host,port))  
print(s.recv(1024)) 

#server
s = socket.socket()    
host = socket.gethostname()    
port = 9999
s.bind((host,port))   
print("Waiting for connection...")  
s.listen(5)  
while True:
    conn,addr = s.accept()  
    print('Got Connection from', addr)
    conn.send(b'Responce From the Server')
    print("Message sent")
    conn.close()
    s.close()
    