import sys
from PySide6.QtWidgets import (QWidget, QPushButton, QApplication, 
                             QGridLayout, QLCDNumber)
import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"

class Example(QWidget):
    cash_queue = 0    
    credit_cards_queue = 0
    other_transactions_queue = 0
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        self.setGeometry(750, 300, 400, 300)
        self.setWindowTitle('QGridLayout-QLCDNumber-calculator')

        grid = QGridLayout()
        self.setLayout(grid)        

        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd, 0, 0, 3, 0)
        grid.setSpacing(10)


        self.show()
    def on_message_cash(self, client, userdata, message): 
        self.cash_queue = self.cash_queue + 1
        print("A" + str(self.cash_queue))
        self.lcd.display(message.payload.decode("utf-8"))
    


if __name__ == '__main__':
   if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    cashierWindow = Example()
    mqtt_client = mqtt.Client()
    mqtt_client.connect("test.mosquitto.org", 1883)
    mqtt_client.on_message = cashierWindow.on_message_cash
    mqtt_client.subscribe("clients/cash")
    mqtt_client.loop_start()
    app.exit(app.exec_())