"""
 * 
 *  Created on: Jul 24, 2021
 *  Last modified on: Jul 24, 2021
 *      Author: Leonardo Alfaro
 *      Last modifier: Leonardo Alfaro
 *
 *  Description: This file describes the cashier in the bank, it can receive requests for any of the booths, accept them 
 *

"""

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QMainWindow
import paho.mqtt.client as mqtt
import queue

import sys

broker = "test.mosquitto.org"






class cashier(QMainWindow):
    cash_queue = 0    
    credit_cards_queue = 0
    other_transactions_queue = 0

    def __init__(self):
        mqtt_client = mqtt.Client()
        super(cashier, self).__init__()
        self.setGeometry(800, 400, 800, 400)
        self.setWindowTitle("Clients ready to be taken")
        self.initUI()
        
        #cash_queue = 0
        #credit_cards_queue = 0
        #other_transactions_queue = 0

    # This function controls buttons, labels and its properties
    def initUI(self):

        # Font for the numbers
        

        numbers_font_size = self.font()
        numbers_font_size.setPointSize(46)

        # Label for the cash queue
        self.cashlabel = QtWidgets.QLabel(self)
        self.cashlabel.setText("Clients waiting for a cash deposit")
        self.cashlabel.setGeometry(50,50, 200, 30)
        # Label for the credit cards queue
        self.creditCardsLabel = QtWidgets.QLabel(self)
        self.creditCardsLabel.setText("Clients waiting for credit cards")
        self.creditCardsLabel.setGeometry(350, 50, 200, 30)
        # Label for the other transactions queue
        self.otherTransactionsLabel = QtWidgets.QLabel(self)
        self.otherTransactionsLabel.setText("Clients waiting for other transactions")
        self.otherTransactionsLabel.setGeometry(600,50, 200, 30)

        #### Label that shows the number of clients waiting for each queue ###

        self.cash_queue_number = QtWidgets.QLabel(self)
        #self.MyFont = QtGui.QFont("Arial", 150)
        #self.cash_queue_number.setFont(self.MyFont)
        #self.layout.addWidget(self.cash_queue_number)
        self.cash_queue_number.setFont(numbers_font_size)
        self.cash_queue_number.setText("0")
        self.cash_queue_number.setGeometry(100, 150, 100, 100)

        self.creditCards_queue_number = QtWidgets.QLabel(self)
        self.creditCards_queue_number.setFont(numbers_font_size)
        self.creditCards_queue_number.setText("0")
        self.creditCards_queue_number.setGeometry(350, 150, 100, 100)

        self.otherTransactions_queue_number = QtWidgets.QLabel(self)
        self.otherTransactions_queue_number.setFont(numbers_font_size)
        self.otherTransactions_queue_number.setText("0")
        self.otherTransactions_queue_number.setGeometry(650, 150, 100, 100)


        # Buttons
        # Define this button properties like the text in it, size and location
        self.cashButton = QtWidgets.QPushButton(self)
        self.cashButton.setText("Take a client for the cash queue")
        self.cashButton.setGeometry(10,300, 200, 30)
        # Connect this button to the function that it is supposed to trigger
        self.cashButton.clicked.connect(self.getNumberCashQueue)
        # Event function, gets triggered every time we press the button 

        self.creditCardsButton = QtWidgets.QPushButton(self)
        self.creditCardsButton.setText("Take a client for the credit card queue")
        self.creditCardsButton.setGeometry(280,300, 220, 30)
        
        self.otherTransactionsButton = QtWidgets.QPushButton(self)
        self.otherTransactionsButton.setText("Take a client for the other transactions queue")
        self.otherTransactionsButton.setGeometry(550,300, 270, 30)

    def getNumberCashQueue(self):
        print("You got a number for the cash queue, your number is ")
    
    # Change the label for the cash queue when a new client requests assistance 
    def on_message_cash(self, client, userdata, message): 
        self.cash_queue = self.cash_queue + 1
        print("A" + str(self.cash_queue))
        self.cashlabel.setText(str(message.payload.decode("utf-8")))

    def on_message_credit(self, client, userdata, message):
        print("credit cars")

    def on_message_other(self, client, userdata, message):
        print("other")

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    cashierWindow = cashier()
    mqtt_client = mqtt.Client()
    mqtt_client.connect("test.mosquitto.org", 1883)
    mqtt_client.on_message = cashierWindow.on_message_cash
    mqtt_client.subscribe("clients/cash")
    mqtt_client.loop_start()

    

# Interface function with labels and buttons
def cashierWindow():

    window = cashier()
    window.setGeometry(800, 300, 850, 400)
    window.setWindowTitle("Please select which transaction you wish to request")
    window.show()
    sys.exit(app.exec())

cashierWindow()


    
