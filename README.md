anyio3: A Python 3 anyio replacement using either RPi.GPIO or pymata-aio
=====

Reasons to use anyio3 instead of anyio:
* Works in Python 3
* Speaks the [Firmata](https://github.com/firmata) protocol over USB.
  * Firmata supports digital and analog GPIO, PWM, I2C, accurate timing, and much more!
  * Upgrade to these features at any time using [pymata-aio](https://github.com/MrYsLab/pymata-aio)
  * Remain compatible with anyio scripts after upgrading without changing your firmware.
* Uses the "StandardFirmataPlus" [Arduino firmware](https://github.com/firmata/arduino) available with the Arduino toolkit.
* Plug-and-play detection of your Arduino Firmata device.
* Single import auto-detects RaspberryPi and Firmata Arduino device, or falls back to a console simulator.
  * Determine which module is loaded by comparing GPIO.hardware to GPIO.RPI, GPIO.PYMATA, and GPIO.CONSOLE.

This project replaces anyio with a module that is compatible with Python 3 and uses the Firmata protocol and firmwares.
The original [anyio](https://github.com/whaleygeek/anyio) package developed by David Whale allows developers without a RaspberryPi to simulate digital GPIO pins or use the digital GPIO pins of a 3.3v Arduino attached via USB.
The excellent "Adventures in Minecraft" book uses anyio to teach children simple electronics projects that interact with Minecraft for RaspberryPi or appropriate simulator mod.

The anyio package simulates the 5 most common functions of the RPi.GPIO interface.
These functions are either connected to a console GPIO simulator or to the anyio Arduino firmware implementing the anyio serial protocol.
While the anyio firmware and protocol are sufficient to run the exercises in the book, they are very limited.
The anyio package does not support analog pins, I2C, or PWM and the serial protocol and firmware reflect these limitations.
Additionally there have been reported difficulties running anyio in Python 3.

A solution to these problems already exists.
[Firmata](https://github.com/firmata) is a advanced GPIO serial protocol and there is an [Arduino firmware](https://github.com/firmata/arduino) available.
Better still, Firmata is available for many hardware platforms; there is even ongoing work to build a [Firmata Firmware for RaspberryPi](https://www.npmjs.com/package/firmata-pi) .
The [pymata-aio](https://github.com/MrYsLab/pymata-aio) package provides Python 3 with a rich interface to any Firmata device.
Moving forward, Firmata should be the serial protocol and firmware of choice.
Python developers should be using pymata-aio directly to interact with hardware in an abstract way.

Developers learning Python from "Adventures in Minecraft" will still need access to an anyio-like library as they learn.
As they advance, older anyio programs should continue to work alongside pymata-aio programs while using the same firmware and serial protocol.
This project bridges that gap by using pymata-aio to provide a compatible anyio interface while remaining easy to use.

Installation
-----

If you are using an Arduino, you must install the "StandardFirmataPlus" firmware onto your Arduino.
This firmware is included in the [Arduino IDE](https://www.arduino.cc/en/Main/Software) and can be opened by *File -> Examples -> Firmata -> StandardFirmataPlus*.
Simply upload that firmware using the instructions that came with your Arduino.

The python dependencies required vary by your base platform.
RaspberryPi users should ensure that a package defining 'RPi.GPIO' is installed.
I believe the current package is 'RPIO'.
To do this, run the following command:

~~~ sh
pip install RPIO
~~~

Arduino users should ensure that 'pymata-aio' is installed.
To do this, run the following command:

~~~ sh
pip install pymata-aio
~~~

To use anyio3, simply copy the *anyio3* directory to your minecraft script directory.
I highly recommend using the [Rasperry Jam Mod](https://github.com/arpruss/raspberryjammod) for all desktop computers.
It contains a pre-configured script folder in *.minecraft/mcpipy* where you should install *anyio3*.
In addition to being very easy to configure, the RaspberyJamMod allows you to run your scripts within Minecraft using the **/py** command.

Console Simulator
-----

The console simulator works differently from the anyio package.
The simulator will output all of the states of your pins when it starts and will then wait for a line of input.
For each character entered that matches a named pin, it will toggle that pin's digital state.
When all characters have been processed, the simulator will print the current GPIO state.
If any simulated GPIO function is invoked, it will take appropriate action and print the current GPIO state.

Known issues and Bugs
-----

The Python GUI, called "IDLE", does not preserve multi-threading.
If you are using the console simulator, please run your program from a true console.

If you have any problems, please use the [GitHub issue tracker for anyio3](https://github.com/doerrie/anyio3/issues).

Additional Notes
-----

If you are still using Python 2 and would like to use Firmata, please consider using [this fork of the anyio repository](https://github.com/doerrie/anyio).

The bukkit mod and canary mod frameworks for Minecraft are no longer maintained due to licensing issues.
If you are having difficulty getting these mods working for current Minecraft versions, consider using the [Rasperry Jam Mod](https://github.com/arpruss/raspberryjammod).

I also have a [mini-howto](AdvInMCFromScratch.md) build your own Adventures in Minecraft Starter Kit from Scratch using GitHub software.
