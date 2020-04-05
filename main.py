# AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9
import gc
import time

import config
import machine
import ubinascii
import ujson
from callback import sub_callback
from robust import MQTTClient, ReConnectError
from status import InternalLed
from wifi import do_connect, get_network

mqtt_client = None

def connect_mqtt():
    global mqtt_client

    try:
        with open(config.KEY_FILE, "r") as f:
            key = f.read()
        print("Got Key")
        with open(config.CERT_FILE, "r") as f:
            cert = f.read()
        print("Got Cert")

        mqtt_client = MQTTClient(
            client_id=config.MQTT_CLIENT_ID, server=config.MQTT_HOST, port=config.MQTT_PORT,
            keepalive=5000, ssl=True, 
            ssl_params={"cert": cert, "key": key, "server_side": False}
        )
        mqtt_client.set_callback(sub_callback)
        mqtt_client.connect()
        mqtt_client.subscribe(config.MQTT_TOPIC)
        print('MQTT Connected')

    except Exception as e:
        print('Cannot connect MQTT: ' + str(e))
        raise

def publish_online():
    global mqtt_client
    mqtt_client.publish(
        config.MQTT_TOPIC, 
        ujson.dumps({
                "state": 'connected',
                "device_type": "ESP32-CAM",
                "device": ubinascii.b2a_base64(machine.unique_id()),
            }
        )
    )

print("Connecting MQTT")
connect_mqtt()
publish_online()

print("SYSTEM OK")

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  if config.DEBUG:
    print('DEBUG Mode, Manual restart required')
  else:
    time.sleep(10)
    machine.reset()

if not mqtt_client.connect(clean_session=False):
    print("New session being set up")
    mqtt_client.subscribe(config.MQTT_TOPIC)

while 1:
    try:
        mqtt_client.wait_msg()
    except Exception as e:
        status = InternalLed()
        status.setError()
        print(e)
        restart_and_reconnect()
        
mqtt_client.disconnect()
