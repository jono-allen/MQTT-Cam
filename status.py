import machine


class InternalLed():
    def __init__(self):
        p4 = machine.Pin(4)
        self.led = machine.PWM(p4, freq=0, duty=0)
    
    def setConnecting(self):
        self.led.freq(1)
        self.led.duty(1)

    def setError(self):
        self.led.freq(500)
        self.led.duty(1)
    
    def clear(self):
        self.led.freq(0)
        self.led.duty(0)

    def setFull(self):
        self.led.freq(1000)
        self.led.duty(1000)
