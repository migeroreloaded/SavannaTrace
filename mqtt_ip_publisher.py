import time
import socket
import paho.mqtt.client as mqtt

MQTT_BROKER_HOST = "broker.emqx.io"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = "ip_address_topic"
RETRY_INTERVAL = 5  # seconds

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        publish_ip_address(client)
    else:
        print(f"Failed to connect to MQTT broker. Retrying in {RETRY_INTERVAL} seconds...")
        time.sleep(RETRY_INTERVAL)
        client.reconnect()

def publish_ip_address(client):
    ip_address = socket.gethostbyname(socket.gethostname())
    client.publish(MQTT_TOPIC, ip_address)
    print(f"Published IP address: {ip_address}")

client = mqtt.Client()
client.on_connect = on_connect

while True:
    try:
        client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
        break
    except:
        print(f"Failed to connect to MQTT broker. Retrying in {RETRY_INTERVAL} seconds...")
        time.sleep(RETRY_INTERVAL)

client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()