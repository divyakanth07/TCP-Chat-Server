import socket
import threading
import base64

host = '127.0.0.1'
port = 4545

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
usernames = []

def broadcast(message):
    encoded_message = base64.b64encode(message)
    for client in clients:
        client.send(encoded_message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            decoded_message = base64.b64decode(message)
            broadcast(decoded_message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'{username} got slapped with a Pizza so hard they flew to the moon.'.encode('ascii'))
            usernames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()
        print("{} made a pact with the devil and sold their soul!!!".format(str(address)))

        client.send(base64.b64encode('USERN'.encode('ascii')))
        username = base64.b64decode(client.recv(1024)).decode('ascii')
        usernames.append(username)
        clients.append(client)

        print("Username is {}".format(username))
        broadcast("{} joined!".format(username).encode('ascii'))
        client.send(base64.b64encode('Joined our Cul-De-Sac'.encode('ascii')))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
