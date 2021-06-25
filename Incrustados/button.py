import paho.mqtt.client as mqtt
# import sys
# from PySide6.QtWidgets import QApplication, QPushButton
# from PySide6.QtCore import Slot

# MAX_CLIENT = 1000
# CASHBOX = "1"
# PLATAFORM = "2"
# CREDIT = "3"
broker = "test.mosquitto.org"
# client_counter = 0
client = mqtt.Client()
client.connect(broker, 1883, 60)
client.publish("clientes/cajas", "100")

# @Slot()
# def cashbox(client_counter):
#     print("cajas")
#     client.publish("clientes/cajas", CASHBOX)
#     if(client_counter >= 1000):
#         client_counter = 0
#     else:
#         client_counter += 1
#     client.publish("clientes/tiquete", client_counter)
# @Slot()
# def plataform(client_counter):
#     print("plataforma")
#     client.publish("clientes/plataforma", PLATAFORM)
#     if(client_counter >= MAX_CLIENT):
#         client_counter = 0
#     else:
#         client_counter += 1
#     client.publish("clientes/tiquete", client_counter)
# @Slot()
# def credit(client_counter):
#     print("credito")
#     client.publish("clientes/credito", CREDIT)
#     if(client_counter >= 1000):
#         client_counter = 0
#     else:
#         client_counter += 1
#     client.publish("clientes/tiquete", client_counter)
    



# # Create the Qt Application
# app = QApplication(sys.argv)
# # Create a button, connect it and show it
# button = QPushButton("Click me")
# button.clicked.connect(cashbox)
# button.show()

# button2 = QPushButton("Plataforma")
# button2.clicked.connect(plataform)
# button2.show()

# # Run the main Qt loop
# app.exec()