import ujson

from .action import Action


class ActionTypes:
    def __init__(self):
        self.LED_STATE = 'led_state'
        self.CAPTURE_IMAGE = 'capture_image'


def sub_callback(topic, msg):
    msg_json = ujson.loads(msg)
    action = Action(msg_json)
    action_types = ActionTypes()

    if 'type' in msg_json and msg_json['type'] == action_types.LED_STATE:
        action.blink_led()
    if 'type' in msg_json and msg_json['type'] == action_types.CAPTURE_IMAGE:
        print('Capture Image')
        action.handle_capture()
    
    print('Callback complete')
