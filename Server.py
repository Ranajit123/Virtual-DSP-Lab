import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtNetwork import QTcpServer, QHostAddress
from AudioPlot import audioPlot
from IIRFilter import IIRaudioPlot
from FIRFilter import FIRaudioPlot
import pickle

HOST = "0.0.0.0"
PORT = 12345
class ServerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Server")
        self.setFixedSize(300, 70)

        self.label = QLabel("Server is running.")
        self.label1 = QLabel("Waiting for create connection with client..")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        self.setLayout(layout)

        self.server_socket = QTcpServer()
        self.server_socket.newConnection.connect(self.accept_connection)
        self.server_socket.listen(QHostAddress(HOST), PORT)

    def accept_connection(self):
        self.client_socket = self.server_socket.nextPendingConnection()
        client_ip_address = self.client_socket.peerAddress().toString()
        if(client_ip_address == "192.168.109.171"):
            self.label.setText(f"Server is Connected With: Ranajit Das")
        self.label1.setText("Waiting for audio duration..")
        self.client_socket.readyRead.connect(self.read_data_from_client)

    def read_data_from_client(self):
        self.message = self.client_socket.readAll().data().decode()
        self.label1.setText(f"Audio Duration: {self.message} Sec")
        self.duration = self.message
        if self.message == "Original Audio":
            self.send_function()
        elif self.message == "IIRFilter":
            self.IIRFilterPlot()
        elif self.message == "FIRFilter":
            self.FIRFilterPlot()
    
    def send_function(self):
        self.label1.setText(f"Plot: {self.message}")
        Original_Audio_Function = pickle.dumps(audioPlot)
        self.client_socket.write(Original_Audio_Function)

    def IIRFilterPlot(self):
        self.label1.setText(f"Filter Type : {self.message}")
        IIR_Audio_Function = pickle.dumps(IIRaudioPlot)
        self.client_socket.write(IIR_Audio_Function)

    def FIRFilterPlot(self):
        self.label1.setText(f"Filter Type : {self.message}")
        FIR_Audio_Function = pickle.dumps(FIRaudioPlot)
        self.client_socket.write(FIR_Audio_Function)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    server_window = ServerWindow()
    server_window.show()
    sys.exit(app.exec_())
