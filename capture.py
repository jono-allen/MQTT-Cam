import time

import camera


def take_photo():
    try:
        camera.init()
    except Exception as e:
        print(e)
    time.sleep(2)
    buff = camera.capture()
    time.sleep(2)
    try:
        camera.deinit()
    except Exception as e:
        print(e)
    
    return buff
