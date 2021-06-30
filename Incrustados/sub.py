import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Se conecto con mqtt " + str(rc))
    client.subscribe("clients/cash")


def on_message(client, userdata, msg):
    if msg.topic == "clients/cash":
        print(f"Cliente es: {str(msg.payload)}")
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()