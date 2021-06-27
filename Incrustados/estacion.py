import paho.mqtt.client as mqtt
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon


MAX_CLIENT = 1000
MAX_QUEUE = 100
broker = "test.mosquitto.org"

client = mqtt.Client()
client.connect(broker, 1883, 60)


#Aquí va la lógica de botones, donde si se toca un boton, estado = boton
#QWidget
class Window(QMainWindow):
    client_counter = 0
    cashbox_count = 0
    plataform_count = 0
    credit_count = 0

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(800, 400, 800, 400)
        self.setWindowTitle("Clients ready to be taken")
        self.home()
    def home(self):
        
        # Label for the cash queue
        self.cashlabel = QtWidgets.QLabel(self)
        self.cashlabel.setText("Cash deposit")
        self.cashlabel.move(50,50)
        # Label for the credit cards queue
        self.creditCardsLabel = QtWidgets.QLabel(self)
        self.creditCardsLabel.setText("Credit cards")
        self.creditCardsLabel.move(350, 50)
        # Label for the other transactions queue
        self.otherTransactionsLabel = QtWidgets.QLabel(self)
        self.otherTransactionsLabel.setText("Plataform")
        self.otherTransactionsLabel.move(650,50)

        # Buttons
        # Define this button properties like the text in it, size and location
        self.cash_button = QtWidgets.QPushButton(self)
        self.cash_button.setText("Number for the cash queue")
        self.cash_button.setGeometry(10,100, 200, 30)
        

        self.credit_button = QtWidgets.QPushButton(self)
        self.credit_button.setText("Number for the credit card queue")
        self.credit_button.setGeometry(280,100, 220, 30)
        
        self.plataform_button = QtWidgets.QPushButton(self)
        self.plataform_button.setText("Number for plataform queue")
        self.plataform_button.setGeometry(550,100, 270, 30)

        #Action made by the buttons when triggered
        self.cash_button.clicked.connect(self.cashbox)
        self.plataform_button.clicked.connect(self.plataform)
        self.credit_button.clicked.connect(self.credit)
        
        self.cash_button.setIcon(QIcon("./red.png"))
        self.plataform_button.setIcon(QIcon("./red.png"))
        self.credit_button.setIcon(QIcon("./red.png"))
        # Run the main Qt loop
        self.show()

    def cashbox(self):
        print("cajas")
        
        client.publish("clients/cash", self.cashbox_count)
        if(self.client_counter >= MAX_CLIENT):
            self.client_counter = 0
        if(self.cashbox_count >= MAX_QUEUE):
            self.cashbox_count = 0
        else:
            self.cashbox_count += 1
            self.client_counter += 1
        client.publish("clientes/tiquete", self.client_counter)
        

    def plataform(self):
        print("plataforma")
        client.publish("clientes/plataforma", self.plataform_count)
        if(self.client_counter >= MAX_CLIENT):
            self.client_counter = 0
        if(self.plataform_count >= MAX_QUEUE):
            self.plataform_count = 0
        else:
            self.client_counter += 1
            self.plataform_count += 1
        client.publish("clientes/tiquete", self.client_counter)


    def credit(self):
        print("credito")
        client.publish("clientes/credito", self.credit_count)
        if(self.client_counter >= 1000):
            self.client_counter = 0
        if(self.credit_count >= MAX_QUEUE):
            self.credit_count = 0
        else:
            self.client_counter += 1
            self.cashbox_count += 1
        client.publish("clientes/tiquete", self.client_counter)

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

def cashierWindow():
    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(800, 300, 850, 400)
    window.setWindowTitle("Please select which transaction you wish to request")
    
    window.show()
    sys.exit(app.exec())

cashierWindow()








