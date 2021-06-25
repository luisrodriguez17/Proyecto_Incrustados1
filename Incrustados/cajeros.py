import paho.mqtt.client as mqtt
import time


CAJA = 1
PLATAFORMA = 2
CREDITO = 3

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)


def caja():
    client.publish("clientes/cajas","1")

def plataforma():
    client.publish("clientes/plataforma","2")

def credito():
    client.publish("clintes/credito","3")


case = {
        1 : caja,
        2 : plataforma,
        3 : credito,

}