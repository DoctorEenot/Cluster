import socket
import threading
import time

"""
Files with scripts must be called 0.py ; 1.py ; ...
"""


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
    ans = connections[id][0].recv(2048)
    file = open('out'+str(id),'w')
    file.write(str(ans))
    file.close()
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
    
    count = input("Num of scripts: ")
    events = []
    threads = []
    if count <= len(connections):
        for i in range(count):
            events.append(threading.Event())
        for i in range(count):
            threads.append(threading.Thread(target=SendProg,args=(str(i)+'.py',i)))
        for i in range(count):
            threads[i].start()
            events[i].send()
        for i in range(count):
            threads[i].join()
    else:
        print('Not enough connections, will be repaired soon.')
    ans = SendProg('hash.py',0)
    print(ans)

    

main()