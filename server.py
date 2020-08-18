#threading means running multiple tasks/function calls at the same time
# import sys
import socket
from _thread import*
#To become local host, meaning anything on our WiFi network that can see each other, but outside of it does not work
#type cd \windows\system32 to cmd and ipconfig next
server='192.168.1.10'
port=5555
#Type of connection, how the server string comes in
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #will bind to whatever IP address, we'll put in here
    s.bind((server,port))
except socket.error as e:
    str(e)
#start listening for connections
#opens up the port & start connecting to it and having multiple clients
#blank parenthesis means allow unlimited connections
s.listen(2)
print('Waiting for a connection, Server Started')

def read_pos(str):
    str=str.split(",")
    return int(str[0]),int(str[1])
def make_pos(tupl):
    return str(tupl[0])+','+str(tupl[1])
#hold positions of players
pos = [(0,0),(100,100)]

def threaded_client(conn,player):
    #conn.send(str.encode('Connected'))
    conn.send(str.encode(make_pos(pos[player])))
    reply=""
    while True:
        try:
            #if errored, increase size, bigger take longer
            #everytime receive, send back with readable tuple
            data = read_pos(conn.recv(2048).decode())
            #b/c whenever sending info. over a like client-server system, info encoded
            pos[player]=data
                #reply = data.decode("utf-8")
            #if we try to get some info from the what decode the client and get nothing, disconnect
            if not data:
                print('Disconnected')
                break
            else:
                if player==1:
                    reply=pos[0]
                else:
                    reply=pos[1]

                #print('Received: ',reply)
                print('Received: ',data)
                print('Sending:', reply)
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print('Lost connection')
    conn.close()

#need to track positions
#Everytime we create new connection/accept new connection, add one to our current player

currentPlayer=0
while True:
    #continuously listening for connection
    #This will accept any incoming connections
    #conn for storing the connection, and addr for IP address
    #combined is an object representing what is connected
    conn, addr=s.accept()
    print('Connected to:',addr)
    start_new_thread(threaded_client,(conn,currentPlayer))
    #tracking which player we are using
    currentPlayer+=1