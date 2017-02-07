# This implements the console GPIO interface as a class.
#
# This class simulates 26 GPIO pins on the console
# When the class is instantiated

import sys
import threading

LOW = 0
HI = 1

IN = 0
OUT = 1

BRD = 0
BCM = 1

class CommandInput(threading.Thread):
    def __init__(self,gpio):
        super(CommandInput, self).__init__()
        self.gpio = gpio

    def run(self):
        while True:
            command = input().strip()
            for c in command:
                pin = ord(c)-ord('a')
                self.gpio._togglePin(pin)
            self.gpio._refresh()

class GpioClass:

    def __init__(self, num_pins=26):
        self._lock = threading.Lock()
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
        self.t = CommandInput(self)
        self.t.start()
        pass

    def _pinHi(self, pin):
        return pin == True or pin == self.HI or pin == 1

    def _togglePin(self, pin):
        if self.pin_states[pin] == self.IN:
            if self._pinHi(self.pin_values[pin]):
                self._output(pin, self.LOW)
            else:
                self._output(pin, self.HI)

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

    def _output(self, channel, value):
        v = self.LOW
        if self._pinHi(value):
            v = self.HI
        self.pin_values[channel]=v

    def output(self, channel, value):
        self._output(channel, value)
        self._refresh()

    def cleanup(self):
        pass

    def _refresh(self):
        with self._lock:
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
