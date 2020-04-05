# # This works for either ESP8266 ESP32 if you rename certs before moving into /flash
CERT_FILE = "/flash/cert"
KEY_FILE = "/flash/priv-key"

# if you change the ClientId make sure update AWS policy
MQTT_CLIENT_ID = ""
MQTT_PORT = 8883

# if you change the topic make sure update AWS policy
MQTT_TOPIC = "my/Example/Topic"

# Change the following three settings to match your environment
MQTT_HOST = "my.mqtt.host"

DEBUG=False
INSTALL_DEPS=False

WIFI_SSID = ""
WIFI_PW = ""
