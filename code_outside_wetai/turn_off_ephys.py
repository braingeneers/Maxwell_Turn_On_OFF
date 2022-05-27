#!/usr/bin/env python3
# Author: melliot1@ucsc.edu
# Summary: This python file turns off the ephys environment for controling the MaxOne from WetAI.
# Run Command: python3 /home/mxwbio/wetai/Projects/Maxwell_Turn_On_OFF/code_outside_wetai/turn_off_ephys.py

import os                                                                   # used to run terminal bash commands
import uuid                                                                 # uuid & messaging used for IoT
from braingeneers.utils import messaging

if __name__ == '__main__':
    print("turning off ephys")
    mb = messaging.MessageBroker( str(uuid.uuid4()) )                       # set up iot
    os.system("/home/mxwbio/MaxLab/bin/killall.sh")                         # shut down MaxOne server
    os.system("echo mxwbio | sudo -S docker stop wetai")                    # stop wetai
    mb.publish_message(topic="mcclintock/cmnd/POWER", message="OFF" )       # turn off smart plug
