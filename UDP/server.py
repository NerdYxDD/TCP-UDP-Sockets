import socket, time

host = "localhost"
port = 6969

clients = []

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind((host, port))

quit = False
print('Server has STARTED...')

while not quit:
    try:
        data, addr = server_sock.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        client_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print(addr[0] + ':' + str(addr[1]) + ', ' + client_time + ' | ', end='')
        print(data.decode("utf-8"))

        server_msg = input("Server:: ")
        for client in clients:
            if addr != client:
                server_sock.sendto(data, client)
            server_sock.sendto(server_msg.encode("utf-8"), client)
    except KeyboardInterrupt:
        quit = True
        print('\nServer has STOPPED...')

server_sock.close()