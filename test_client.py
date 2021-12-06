from sock import Socket
import threading

class Client(Socket):
    def __init__(self):
        super(Client, self).__init__()
    
    def set_up(self):
        self.connect(('127.0.0.1', 1234))

        listen_thread = threading.Thread(target=self.listen_socket)
        listen_thread.start()

        send_thread = threading.Thread(target=self.send_data, args=(None,))
        send_thread.start()

    def listen_socket(self, listened_socket=None):
        while True:
            data = self.recv(2048)
            print(data.decode('utf-8'))

    def send_data(self, data):
        while True:
            self.send(data.encode('utf-8'))

if __name__ == '__main__':
    client = Client()
    client.set_up()