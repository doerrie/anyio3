# This implements the pymata3 GPIO interface as a class.
#
# This class allows you to manually specify a COM port from your code.
#
# Yes, it really is this simple to use pymata_aio.pymata3.
# Consider using it directly.

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

LOW = 0
HI = 1

IN = Constants.INPUT
OUT = Constants.OUTPUT

BRD = 0
BCM = 1

class GpioClass:

    def __init__(self, com_port=None, arduino_wait=5):
        self.board = PyMata3(com_port=com_port, arduino_wait=arduino_wait)
        self.LOW = LOW
        self.HI = HI
        self.IN = IN
        self.OUT = OUT
        self.BRD = BRD
        self.BCM = BCM
        pass

    def setmode(self, mode):
        pass

    def setup(self, channel, mode):
        self.board.set_pin_mode(pin_number=channel, pin_state=mode)

    def input(self, channel):
        return self.board.digital_read(pin=channel)

    def output(self, channel, value):
        self.board.digital_write(pin=channel, value=value)

    def cleanup(self):
        pass
