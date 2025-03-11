import socket
import threading
import base64

host = '127.0.0.1'
port = 4545

username = input("> What would you like being called : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024)
            decoded_message = base64.b64decode(message).decode('ascii')
            if decoded_message == 'USERN':
                client.send(base64.b64encode(username.encode('ascii')))
            else:
                print(decoded_message)
        except:
            print("Someone Messed UP@!!")
            client.close()
            break

def write():
    while True:
        message = '>{}: {}'.format(username, input(''))
        encoded_message = base64.b64encode(message.encode('ascii'))
        client.send(encoded_message)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
