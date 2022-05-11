import socket, time
from threading import Thread

key = 8194

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(("localhost", 6856))

def listen_server():
    while True:
        data = client_sock.recv(1024)
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

def send_server():
    listen_thread = Thread(target=listen_server)
    listen_thread.start()
    name = input("Please enter your name: ")

    while True:
        msg = input(f"{name}:: ")

        crypt = ""
        for i in msg:
            crypt += chr(ord(i) ^ key)
        msg = crypt

        client_sock.send((name + ":: " + msg).encode("utf-8"))

send_server()