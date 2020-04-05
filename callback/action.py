from exceptions import UploadError

import uploader
from capture import take_photo
from machine import Pin


class Action:
    def __init__(self, msg_json):
        self.msg_json = msg_json

    def handle_capture(self):
        if 'payload' not in self.msg_json:
            raise UploadError('Data has no payload')
        payload = self.msg_json['payload']
        buff = take_photo()
        data, headers = uploader.make_request(payload['fields'], buff)
        try:
            uploader.upload_image(payload['url'], headers=headers, data=data)
        except UploadError as upload_error:
            raise
        print('Uploading request success')

    def blink_led(self):
        led = Pin(4, Pin.OUT)
        if self.msg_json['state'] is True:
            led.value(1)
        else:
            led.value(0)
