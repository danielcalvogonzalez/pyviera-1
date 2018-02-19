#!/usr/bin/python

from pyviera import Viera, COMMANDS, APPLICATIONS
import sys

def ShowError(msgError):
    print(msgError)
    exit(1)

#
# Check if an argument has been given in the command line
#
if len(sys.argv) != 2:
    ShowError("You need to add the 'command' before using this script")

#
# Check that the command exists
# Either as key or app
#
if sys.argv[1] not in COMMANDS and sys.argv[1] not in APPLICATIONS:
    ShowError("Command '{0}' not found".format(sys.argv[1]))

# Look for any supported TVs
tvs = Viera.discover()

# Make sure we have at least one
if len(tvs) > 0:
    # Get the first TV that was found
    tv = tvs[0]

    # Create the command to execute
    cmd = 'tv.{0}()'.format(sys.argv[1])
    
    exec(cmd)
else:
    print("No TVs could be found")
