#!/usr/bin/env python3
# Author: melliot1@ucsc.edu
# This python file turns on on the ephys environment for controling the MaxOne from WetAI.
# Run command: python3 /home/mxwbio/wetai/Projects/Maxwell_Turn_On_OFF/code_outside_wetai/turn_on_ephys.py

import os                                                         # used to run terminal bash commands
import time                                                       # used to wait for hub/smartplug to start
import uuid                                                       # uuid & messaging used for IoT
from braingeneers.utils import messaging

if __name__ == '__main__':    
    print("turning on ephys. Please wait 7 seconds.")
    mb = messaging.MessageBroker( str(uuid.uuid4()) )                 # set up iot
    mb.publish_message(topic="mcclintock/cmnd/POWER", message="ON" )  # turn on smart plug
    time.sleep(7)                                                     # wait 7 seconds for smart plug
    os.system("echo mxwbio | sudo -S docker start wetai")             # turn on wetai
    os.system("/home/mxwbio/MaxLab/bin/mxwserver.sh &")               # turn on maxwell server
    print("ephys launched!")
    
    