anyio3: A Python 3 anyio replacement using either RPi.GPIO or pymata-aio
=====

This project aims to replace anyio with a module that is compatible with Python 3 and the Firmata protocol.
The [anyio](https://github.com/whaleygeek/anyio) package developed by David Whale simulates the 5 most common functions of the RPi.GPIO interface.
It allows developers without a RaspberryPi to simulate digital GPIO pins or extend their desktop computer with digital GPIO pins using a 3.3v Arduino attached via USB.
His excellent "Adventures in Minecraft" book uses this to teach children simple electronics projects that interact with Minecraft for RaspberryPi or appropriate simulator mod.

Reasons to use anyio3:
* Works in Python 3
* Speaks the [Firmata](https://github.com/firmata) protocol over USB.
  * Firmata supports Digital and Analog GPIO, PWM, I2C, accurate timing, and much more!
  * Upgrade to these features using [pymata-aio](https://github.com/MrYsLab/pymata-aio)
  * Remain compatible with anyio scripts without needing the anyio firmware.
* Uses the "StandardFirmataPlus" [Arduino firmware](https://github.com/firmata/arduino) available with the Arduino toolkit.
* Single import auto-detects RaspberryPi, Firmata Arduino device, or falls back to a console simulator.
  * Determine which module is loaded by comparing GPIO.hardware to GPIO.RPI, GPIO.PYMATA, and GPIO.CONSOLE.


There is even a [developing project](https://www.npmjs.com/package/firmata-pi) to make the RaspberryPi a Firmata device.

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

Arduino users should ensure that pymata-aio is installed.
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

Known issues
-----

The Python GUI, called "IDLE", does not preserve multi-threading.
If you are using the console simulator, please run your program from a true console.

Additional Notes
-----

If you are still using Python 2 and would like to use Firmata, please consider using [this fork of the anyio repository](https://github.com/doerrie/anyio).

The bukkit mod and canary mod frameworks for Minecraft are no longer maintained due to licensing issues.
If you are having difficulty getting these mods working for current Minecraft versions, consider using the [Rasperry Jam Mod](https://github.com/arpruss/raspberryjammod).
