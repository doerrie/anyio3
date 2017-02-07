# A static GPIO wrapper using pymata3

from .GPIOClass import GpioClass, LOW, HI, IN, OUT, BRD, BCM

_gpio = GpioClass()

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
