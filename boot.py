from config import INSTALL_DEPS
from status import InternalLed
from wifi import do_connect, get_network

# start execution
try:
    status = InternalLed()
    status.setConnecting()
    wlan = get_network()
    do_connect(wlan)
    print("Connected WIFI")
    status.clear()
    if INSTALL_DEPS:
        import upip
        upip.install("micropython-urequests")

except Exception as e:
    print(str(e))
    status.setError()
