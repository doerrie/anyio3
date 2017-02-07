anyio3: A Python 3 anyio replacement using either RPi.GPIO or pymata-aio
=====

This project aims to replace anyio with a module that is compatible with Python 3 and the Firmata protocol.
The [anyio](https://github.com/whaleygeek/anyio) package developed by David Whale simulates the 5 most common functions of the RPi.GPIO interface.
It allows developers without a RaspberryPi to simulate digital GPIO pins or extend their desktop computer with digital GPIO pins using a 3.3v Arduino attached via USB.
His excellent "Adventures in Minecraft" book uses this to teach children simple electronics projects that interact with Minecraft for RaspberryPi or appropriate simulator mod.

There are a number of issues with the anyio package and firmware.
The anyio Arduino firmware lacks a lot of features including analog input, PWM, and accurate timing.
[Firmata](https://github.com/firmata) is a standard protocol and [Arduino firmware](https://github.com/firmata/arduino) that supports these features and Python 3 is supported by the [python-aio](https://github.com/MrYsLab/pymata-aio) package.
The anyio protocol and Firmata protocol are not compatible, so upgrading your Arduino with the enhanced firmware will break your old programs.
Additionally, there have been difficulties getting anyio to run in Python 3.

The anyio3 module solves these problems by simulating the anyio functionality using pymata-aio.
It works in Python 3 on either a RaspberryPi or desktop computer.
It will attempt to autodetect your Firmata Arduino without a serial port dance.
When you want access to Firmata features, you can use pymata-aio without altering your Arduino's firmware.
There is even a [developing project](https://www.npmjs.com/package/firmata-pi) to make the RaspberryPi a Firmata device.
I expect that most developers will eventually migrate toward Firmata as it will standardize most of their software.

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
