
import network
from config import WIFI_PW, WIFI_SSID


def get_network():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    return wlan

def do_connect(wlan):
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_PW)

        while not wlan.isconnected():
            pass
    print('Network config:', wlan.ifconfig())
