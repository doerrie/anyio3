anyio3: A Python 3 anyio replacement using either RPi.GPIO or pymata-aio
=====

This project aims to replace anyio with a module that is compatible with Python 3 and the Firmata protocol.
The [anyio](https://github.com/whaleygeek/anyio) package developed by David Whale simulates the 5 most common functions of the RPi.GPIO interface.
It allows developers without a RaspberryPi to simulate digital GPIO pins or extend their desktop computer with digital GPIO pins using a 3.3v Arduino attached via USB.
His excellent "Adventures in Minecraft" book uses this to teach children simple electronics projects that interact with Minecraft for RaspberryPi or appropriate simulator mod.

For owners of an Arduino, the anyio firmware lacks analog support and accurate timing information because these features unavailable on the RaspberryPi.
[Firmata](https://github.com/firmata) is a standard protocol and [Arduino firmware](https://github.com/firmata/arduino) that supports these features and support in Python 3 is provided by the [python-aio](https://github.com/MrYsLab/pymata-aio) package.
The anyio protocol and Firmata protocol are not compatible, so if you upgrade your Arduino all of your previous programs will break.
Additionally, there have been difficulties getting anyio to run in Python 3.
This project was created to address these issues.

This module is intended to work on a RaspberryPi or a PC using an Arduino.
The base GPIO module will import the correct interface for your platform based on what Python modules it can import.
It will try to load RPi.GPIO before loading the pymata-aio interface and searching for an Arduino.
If pymata-aio is not installed or an Arduino running Firmata can not be located, it will exit.

RaspberryPi users should ensure that a package defining 'RPi.GPIO' is installed.
I believe the current package is 'RPIO'.
To do this, run the following command:

~~~ sh
pip install RPIO
~~~

Arduino users should ensure that pymata-aio is installed.
To do this, run the following command:

~~~ sh
pip install pymata-aio
~~~

If you have a package providing simulated RPi.GPIO commands, it will be loaded first.
You can still load the internal class and continue using everything as you might expect.

~~~ python
from anyio3.pymata3.GPIOClass import GpioClass
GPIO = GpioClass()
~~~

You may also specify a serial device and the time it takes for your arduino to reset.
The Leonardo based Arduinos may set arduino_wait to 2.

~~~ python
from anyio3.pymata3.GPIOClass import GpioClass
GPIO = GpioClass(com_port=None, arduino_wait=5)
~~~

---

Additional Notes
-----

If you are still using Python 2 and would like to use Firmata, please consider using [this fork of the anyio repository](https://github.com/doerrie/anyio).

The bukkit mod and canary mod frameworks for Minecraft are no longer maintained due to licensing issues.
If you are having difficulty getting these mods working for current Minecraft versions, consider using the [Rasperry Jam Mod](https://github.com/arpruss/raspberryjammod).
