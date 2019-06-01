import socket
import threading
import time
Port = 765


sock = socket.socket()
sock.bind(('',Port))
connections = []

def fill():
    global connections
    
    print('Waiting for connections...\n')
    sock.listen()
    connections.append(sock.accept())
    print('New connection accepted')

def CheckAlive():
    for i in range(len(sock.accept())):
        try:
            connections[i].send(b'1')
        except:
            connections.remove(connections[i])

def SendProg(FileName,id):
    global connections
    ac = True
    File = open(FileName,'rb')
    cont = File.read()
    prob = 0
    while ac:
        
        connections[id][0].send(bytes(FileName,'utf-8'))
        time.sleep(1)
        connections[id][0].send(cont)
        data = connections[id][0].recv(100)
        
        if data == b'1':
            ac = False
    ans = connections[id][0].recv(1024)
    return ans

def main():
    run = True
    while run:
        e = threading.Event()
        t = threading.Thread(target=fill)
        t.start()
        e.set()
        t.join()
        a = input('Listen? y/n')
        if a == 'n':
            run = False
    
    input("Start?")
    
    ans = SendProg('hi.py',0)
    print(ans)

    

main()