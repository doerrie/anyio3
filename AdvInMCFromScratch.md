Adventures in Minecraft Starter Kit from Scratch in GitHub
=====

To build your own Adventures in Minecraft Starter Kit, you need the following:

* Install the [Rasperry Jam Mod](https://github.com/arpruss/raspberryjammod) using the Windows installer or Zip files.
* Install [anyio3](https://github.com/doerrie/anyio3).
  * Run 'pip install pymata-aio' from the command line.
  * Copy *anyio3* to your *.minecraft/mcpipy* folder.
  * See the [README](https://github.com/doerrie/anyio3/README.md) for more details.
* Download [minecraft-stuff](https://github.com/martinohanlon/minecraft-stuff)
  * Place *minecraftstuff.py* into the *.minecraft/mcpipy/mcpi* folder
  * Copy *LICENSE* as *.minecraft/mcpipy/mcpi/minecraftstuff.py-LICENSE*

You should now have a kit that is compatible with  Adventures in Minecraft with the following caveats:

* Use the 'anyio3' module wherever you would use 'anyio'.
* Use the 'anyio3.GPIO' module wherever you would use 'RPi.GPIO'

As mentioned in the [README](https://github.com/doerrie/anyio3/README.md), you can configure pins for each type of hardware by querying GPIO.hardware for what driver is in use.
