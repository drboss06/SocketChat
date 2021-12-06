import socket
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import threading

#sock = socket.socket()
#sock.connect(('localhost', 9090))

class MyWidget(QMainWindow):
    def __init__(self):
            super().__init__()
            uic.loadUi('cli.ui', self)
            self.sock = socket.socket()
            self.sock.connect(('localhost', 9090))
            self.btn_send.clicked.connect(self.send)
            self.btn_close.clicked.connect(self.close)
        
    def send(self):

        msg = self.text_send.text()
        print(msg)
        self.sock.send(msg.encode('utf-8'))
        data = self.sock.recv(2048)
        self.text_ans.setPlainText(data.decode('utf-8'))
    
    def close(self):
        self.sock.close()
        exit(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())