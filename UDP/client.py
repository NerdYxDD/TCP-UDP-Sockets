import socket, threading, time

key = 8194
shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                decrypt = ''
                k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i) ^ key)
                print(decrypt)
                time.sleep(0.2)
        except:
            pass


host = 'localhost'
port = 0

server = ('localhost', 6969)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.bind((host, port))
client_sock.setblocking(0)

name = input('Please enter your name: ')

rT = threading.Thread(target=receving, args=('RecvThread', client_sock))
rT.start()

while shutdown == False:
    if join == False:
        client_sock.sendto((name + ' => has joined chat ').encode("utf-8"), server)
        join = True
    else:
        try:
            msg = input('Massage is: ')

            crypt = ""
            for i in msg:
                crypt += chr(ord(i) ^ key)
            msg = crypt

            if msg != "":
                client_sock.sendto((name + ':: ' + msg).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            client_sock.sendto((name + ' <= has left chat ').encode("utf-8"), server)
            shutdown = True

rT.join()
client_sock.close()
