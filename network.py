import socket
#from _thread import *
class Network:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server='192.168.1.10'
        self.port=5555
        self.addr=(self.server,self.port)
        self.pos=self.connect()
        #print(self.id)
    def getPos(self):
        return self.pos
    def connect(self):
        try:
            #when we connect return that string connected message encoded
            self.client.connect(self.addr)
            #So need decoding
            return self.client.recv(2048).decode()
        except:
            pass
    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
#b=['a','b','c']
# n = Network()
# print(n.send('hi'))
# print(n.send('work'))
# a=0
# for a in range(0,2):
#     print(n.send(b[a]))
#     print(a)