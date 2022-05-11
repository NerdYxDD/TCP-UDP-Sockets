import socket, threading, time

host = "localhost"
port = 6856

clients = []

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind((host, port))

server_sock.listen(5)
print("Server is LISTENING...")

def start_server():
    while True:
        client_sock, addr = server_sock.accept()

        clients.append(client_sock)

        client_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(addr[0] + ':' + str(addr[1]) + ', ' + client_time + ' | connected!', end='\n')


        listen_accepted_client = threading.Thread(
            target=listen_client,
            args=(client_sock,)
        )
        listen_accepted_client.start()

        

def listen_client(client):
    print("Listening client...")
    while True:
        data = client.recv(1024)
        client_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        print(f"Client sent: {data.decode('utf-8')}, TIME: {client_time}")
        send_all(data)



def send_all(data):
    server_msg = input("Server:: ")
    for client in clients:
        client.send(data)
        client.send(server_msg.encode("utf-8"))

start_server()