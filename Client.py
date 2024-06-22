import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtNetwork import QHostAddress, QTcpSocket
import pickle
from PyQt5.QtCore import QByteArray

HOST = "192.168.29.240"
PORT = 12345

class test(QtWidgets.QMainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    self.ui = uic.loadUi('ClientGUI.ui', self)
# Live Audio Signal Controls 
    self.connect_button.clicked.connect(self.server_connection)
    self.disconnect_button.clicked.connect(self.server_disconnection)
    self.send_button.clicked.connect(self.sendbutton)
    self.start_plot.clicked.connect(self.originalAudio)
    self.IIR_plot.clicked.connect(self.IIRPlot)
    self.FIR_Plot.clicked.connect(self.FIRPlot)

    self.client_socket = QTcpSocket()
    self.client_socket.connected.connect(self.on_connected)
    self.client_socket.disconnected.connect(self.on_disconnected)
    self.client_socket.readyRead.connect(self.receive_function)

# Theoretical Signal Controls 
    self.LPFinput.clicked.connect(self.LPFinputSignal)
    self.BPFinput.clicked.connect(self.BPFinputSignal)
    self.IIRLPF.clicked.connect(self.IIRLPFSignal)
    self.IIRBPF.clicked.connect(self.IIRBPFSignal)
    self.FIRLPF.clicked.connect(self.FIRLPFSignal)
    self.FIRBPF.clicked.connect(self.FIRBPFSignal)

  def server_connection(self):
    ip_address = QHostAddress(HOST)
    self.client_socket.connectToHost(ip_address, PORT)

  def server_disconnection(self):
    self.client_socket.disconnectFromHost()

  def on_connected(self):
    self.label.setText("Connected to the server")

  def on_disconnected(self):
    self.label.setText("Disconnected from the server.")
    self.connect_button.setEnabled(True)

  def sendbutton(self):
    self.label_2.setText("Choose an operation")
    if not self.client_socket.isOpen():
      ip_address = QHostAddress("127.0.0.1")
      port = 12345
      self.client_socket.connectToHost(ip_address, port)

    if self.client_socket.isOpen():
      self.duration = self.Duration_line_edit.text()
      self.client_socket.write(self.duration.encode())

  def receive_function(self):
    data = self.client_socket.readAll().data()
    received_function = pickle.loads(data)
    result = received_function(int(self.duration))

  def originalAudio(self):
    self.client_socket.write(QByteArray("Original Audio".encode()))
    self.label_2.setText(f"Wait for {self.duration} seconds..")

  def IIRPlot(self):
    self.label_2.setText(f"Wait for {self.duration} seconds..")
    self.client_socket.write(QByteArray("IIRFilter".encode()))

  def FIRPlot(self):
    self.label_2.setText(f"Wait for {self.duration} seconds..")
    self.client_socket.write(QByteArray("FIRFilter".encode()))

  def LPFinputSignal(self):
    self.label_3.setText("LPF Input Signal Plotted")
    import LPFInputSignal

  def BPFinputSignal(self):
    self.label_3.setText("BPF Input Signal Plotted")
    import BPFInputSignal

  def IIRLPFSignal(self):
    self.label_3.setText("IIR Filtered LPF Output Signal Plotted")
    import IIRLPFOutputSignal

  def IIRBPFSignal(self):
    self.label_3.setText("IIR Filtered BPF Output Signal Plotted")
    import IIRBPFOutputSignal

  def FIRLPFSignal(self):
    self.label_3.setText("FIR Filtered LPF Output Signal Plotted")
    import FIRLPFOutputSignal

  def FIRBPFSignal(self):
    self.label_3.setText("FIR Filtered BPF Output Signal Plotted")
    import FIRBPFOutputSignal


app = QtWidgets.QApplication(sys.argv)
mainWindow = test()
mainWindow.show()
sys.exit(app.exec_())
