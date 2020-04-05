class UploadError(Exception):
    def __init__(self, response):
        self.response = response

class MQTTException(Exception):
    pass
