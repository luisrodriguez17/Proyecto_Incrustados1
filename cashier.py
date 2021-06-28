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

client = mqtt.Client()
client.connect(broker, 1883, 60)





class cashier(QMainWindow):
    # This queues are for the cashier to see how many clients he has to attend
    cash_queue = 0    
    credit_cards_queue = 0
    other_transactions_queue = 0

    def __init__(self):
        mqtt_client = mqtt.Client()
        super(cashier, self).__init__()
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
        self.cashButton.clicked.connect(self.cashButtonPressed)
        # Event function, gets triggered every time we press the button 

        self.creditCardsButton = QtWidgets.QPushButton(self)
        self.creditCardsButton.setText("Take a client for the credit card queue")
        self.creditCardsButton.setGeometry(280,300, 220, 30)
        self.creditCardsButton.clicked.connect(self.creditCardsButtonPressed)

        
        self.otherTransactionsButton = QtWidgets.QPushButton(self)
        self.otherTransactionsButton.setText("Take a client for the other transactions queue")
        self.otherTransactionsButton.setGeometry(550,300, 270, 30)
        self.otherTransactionsButton.clicked.connect(self.otherTransactionsButtonPressed)

    # Actions for the buttons
    def cashButtonPressed(self):
        print("Taking a client from the cash queue")
        self.cash_queue = self.cash_queue - 1
        self.cash_queue_number.setNum(self.cash_queue)
        client.publish("clients/serving", "A" + str(self.cash_queue))
    
    def creditCardsButtonPressed(self):
        print("Taking a client from the credit cards queue")
        self.credit_cards_queue = self.credit_cards_queue - 1
        self.creditCards_queue_number.setNum(self.credit_cards_queue)

    def otherTransactionsButtonPressed(self):
        print("Taking a client from the other transactions queue")
        self.other_transactions_queue = self.other_transactions_queue - 1
        self.otherTransactions_queue_number.setNum(self.other_transactions_queue)
    
    # Change the label for the cash queue when a new client requests assistance 
    def on_message_cash(self, client, userdata, message): 
        self.cash_queue = self.cash_queue + 1
        self.cash_queue_number.setNum(self.cash_queue)

    def on_message_credit(self, client, userdata, message):
        self.credit_cards_queue = self.credit_cards_queue + 1
        self.creditCards_queue_number.setNum(self.credit_cards_queue)

    def on_message_other(self, client, userdata, message):
        self.other_transactions_queue = self.other_transactions_queue + 1
        self.otherTransactions_queue_number.setNum(self.other_transactions_queue)

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    cashierWindow = cashier()
    cashierWindow.setGeometry(800, 300, 850, 400)
    mqtt_client = mqtt.Client()
    mqtt_client.connect("test.mosquitto.org", 1883)
    mqtt_client.on_message = cashierWindow.on_message_cash # Topic to be subs, basically which transaction
    mqtt_client.subscribe("clients/cash")
    mqtt_client.loop_start()
    cashierWindow.show()
    sys.exit(app.exec())

    

# Interface function with labels and buttons
""" def cashierWindow():

    window = cashier()
    window.setGeometry(800, 300, 850, 400)
    window.setWindowTitle("Please select which transaction you wish to request")
    window.show()
    sys.exit(app.exec())

cashierWindow()
 """

    
