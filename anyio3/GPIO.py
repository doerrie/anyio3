# Automatic GPIO library
#
# This module attempts to be as automatic as possible.
# It attempts to load RPi.GPIO to see if we are using a RaspberryPi.
# If that fails, it attempts to locate an arduino using the pymata3 library.
# TODO: fall back to a simulator instead of failing

import sys

# Prevents nesting
_done = False

# If you would like to force a particular library to load or instantiate a
# class manually, this is the place to do it.  For example, uncomment the
# following two lines to force the pymata3 interface to load.

#from .pymata3.GPIO import *
#_done = True

if not _done:
    try:
        print("Loading RPi.GPIO")
        from RPi.GPIO import *
        print("Success")
        _done = True
    except ImportError:
        print("Failed")
        pass

if not _done:
    try:
        print("Loading .pymata3.GPIO")
        from .pymata3.GPIO import *
        print("Success")
        _done = True
    except ImportError:
        print("")
        print("Failed")
        pass

if not _done:
    try:
        print("Loading .console.GPIO")
        from .console.GPIO import *
        print("")
        print("anyio3 could not automatically locate any hardware on this computer.")
        print("You have been redirected to the console simulator.")
        print("If you do have hardware, please check the anyio3 README and known issues.")
        _done = True
    except ImportError:
        print("Failed")

if not _done:
    print("Could not instantiate a GPIO driver.  Please check your Python environement ...")
    sys.exit(0)
