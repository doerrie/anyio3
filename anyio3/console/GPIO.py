# A static GPIO wrapper

from .GPIOClass import GpioClass, LOW, HI, IN, OUT, BRD, BCM

_gpio = None
try:
    _gpio = GpioClass()
except TypeError:
    pass

def setmode(mode):
    _gpio.setmode(mode)

def setup(channel, mode):
    _gpio.setup(channel, mode)

def input(channel):
    return _gpio.input(channel)

def output(channel, value):
    _gpio.output(channel,value)

def cleanup():
    _gpio.cleanup()
