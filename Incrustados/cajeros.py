import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Se conectó con MQTT"+str(rc))
    client.subscribe("clientes/cajas")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    

client = mqtt.Client()
print("Conectado")
client.on_connect = on_connect
client.on_message = on_message


client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()




