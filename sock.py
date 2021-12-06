import socket

class Socket(socket.socket):
    def __init__(self):
        super(Socket, self).__init__(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
    
    def send_data(self): # Переопределение метода в классе наследнике
        raise NotImplementedError()

    def listen_socket(self, listened_socket=None):
        raise NotImplementedError()
    
    def set_up(self):
        raise NotImplementedError()