# ESP-32 Cam MQTT AWS S3 Uploader

# Download cert and private from device
```
ampy --port /dev/tty.usbmodem14201 --baud 115200 get /flash/cert flash/cert
ampy --port /dev/tty.usbmodem14201 --baud 115200 get /flash/priv-key flash/priv-key
```
# Upload Cert and key to device
```
ampy --port /dev/tty.usbmodem14201 --baud 115200 put /flash/cert flash/cert
ampy --port /dev/tty.usbmodem14201 --baud 115200 put /flash/priv-key flash/priv-key
```

# FlashChip 
```
esptool.py --port /dev/tty.usbmodem14201 erase_flash

esptool.py --chip esp32 --port /dev/tty.usbmodem14201 --baud 115200 write_flash -z 0x1000 esp32-cam-micropython.bin
```