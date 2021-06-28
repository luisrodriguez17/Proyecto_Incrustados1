"""
 * 
 *  Created on: Jul 27, 2021
 *  Last modified on: Jul 27, 2021
 *      Author: Leonardo Alfaro
 *      Last modifier: Leonardo Alfaro
 *
 *  Description: This file is the display that shows the client that must be served and in which queue
 *

"""

import sys
import random

import paho.mqtt.client as mqtt

from PySide6 import QtCore, QtWidgets, QtGui


# Class label (text that shows in the widget)

class MQTTLabel(QtWidgets.QWidget):

    cashQueue = 1
    creditCardsQueue = 1
    otherTransactionsQueue = 1    

    def __init__(self):
        super().__init__()
        # Create an mqtt client
        self.mqtt_client = None

        # Create a label
        # label centered, initial text 0
        self.CurrentClient = QtWidgets.QLabel("0", alignment = QtCore.Qt.AlignCenter)
        # create the font for the label
        self.MyFont = QtGui.QFont("Arial", 150)
        self.fontForServingLabel = QtGui.QFont("Arial", 30)
        # Assigned the font to the previously created label            
        self.CurrentClient.setFont(self.MyFont)
        # Stack different widgets
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.CurrentClient)

        self.nowServingLabel = QtWidgets.QLabel(self)
        self.nowServingLabel.setText("Now serving client:")
        self.nowServingLabel.setFont(self.fontForServingLabel)
        self.nowServingLabel.setGeometry(250, 50, 700, 50)




    # Create a new Mqtt client and pass it to the widget
    def set_client(self, new_mqtt_client):
        # Assign the mqtt client
        self.mqtt_client = new_mqtt_client
    # This function updates the text in the label 
    def on_message_cash_topic(self, client, userdata, message):
        self.CurrentClient.setText("A" + str(self.cashQueue))
        self.cashQueue = self.cashQueue + 1

    def on_message_credit_topic(self, client, userdata, message):
        self.CurrentClient.setText("B" + str(self.creditCardsQueue))
        self.creditCardsQueue = self.creditCardsQueue + 1

    def on_message_other_topic(self, client, userdata, message):
        self.CurrentClient.setText("C" + str(self.otherTransactionsQueue))
        self.otherTransactionsQueue = self.otherTransactionsQueue + 1
# Main

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # Add widgets
    widget = MQTTLabel()
    widget2 = MQTTLabel()

    # Configure MQTT

    mqtt_client = mqtt.Client()
    # Broker and port 1883 is not secure
    mqtt_client.connect("test.mosquitto.org", 1883)
    #When getting a new message call this function
    mqtt_client.on_message = widget.on_message_cash_topic
    # keep listening to the broker
    mqtt_client.loop_start()
    mqtt_client.subscribe("clients/serving")
    widget.set_client(mqtt_client)

    # Stuff for the widgets, window size
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())



