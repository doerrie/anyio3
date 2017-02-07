# This implements the console GPIO interface as a class.
#
# This class simulates 26 GPIO pins on the console
# When the class is instantiated

import sys
import threading
import time

LOW = 0
HI = 1

IN = 0
OUT = 1

BRD = 0
BCM = 1


class GpioClass:

    def __init__(self, num_pins=26):
        self.LOW = LOW
        self.HI = HI
        self.IN = IN
        self.OUT = OUT
        self.BRD = BRD
        self.BCM = BCM
        self.pin_states=[]
        self.pin_values=[]
        for i in range(num_pins):
            self.pin_states.append(self.IN)
            self.pin_values.append(self.LOW)
        pass

    def setmode(self, mode):
        pass

    def setup(self, channel, mode):
        self.pin_states[channel]=mode
        if mode == self.IN:
            self.pin_values[channel]=self.HI
        else:
            self.pin_values[channel]=self.LOW
        self._refresh()

    def input(self, channel):
        return self.pin_values[channel]

    def output(self, channel, value):
        v = self.LOW
        if value == True or value == self.HI or value == 1:
            v = self.HI
        self.pin_values[channel]=v
        self._refresh()

    def cleanup(self):
        pass

    def _refresh(self):
        print("")
        for i in range(len(self.pin_states)):
            print(chr(ord('a')+i), end="")
        print("")
        for state in self.pin_states:
            s = "I"
            if state:
                s = "O"
            print(s, end="")
        print("")
        for value in self.pin_values:
            v = "0"
            if value :
                v = "1"
            print(v, end="")
        print("")
