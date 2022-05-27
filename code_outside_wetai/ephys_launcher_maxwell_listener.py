#!/usr/bin/env python3
# Author: melliot1@ucsc.edu
# Test
# Run command: python3 /home/mxwbio/wetai/Projects/Maxwell_Turn_On_OFF/code_outside_wetai/turn_on_ephys.py

import os                                                         # used to run terminal bash commands
import time                                                       # used to wait for hub/smartplug to start
import uuid                                                       # uuid & messaging used for IoT
from braingeneers.utils import messaging

if __name__ == '__main__':
    
    mb_main = messaging.MessageBroker(str(uuid.uuid4))                # set up iot listener
    q = messaging.CallableQueue()
    mb_main.subscribe_message( topic="ephys_launcher", callback=q )
    while True:
        topic_name, result_message = q.get() #storing the message and the directory name to variables

        if result_message["command"] == "ON":
            print("turning on ephys. Please wait 7 seconds.")
            mb = messaging.MessageBroker( str(uuid.uuid4()) )                 # set up iot
            mb.publish_message(topic="mcclintock/cmnd/POWER", message="ON" )  # turn on smart plug
            time.sleep(7)                                                     # wait 7 seconds for smart plug
            os.system("echo mxwbio | sudo -S docker start wetai")             # turn on wetai
            os.system("/home/mxwbio/MaxLab/bin/mxwserver.sh &")               # turn on maxwell server
            print("ephys launched!")            

        if result_message["command"] == "OFF":
            print("turning off ephys")
            mb = messaging.MessageBroker( str(uuid.uuid4()) )                       # set up iot
            os.system("/home/mxwbio/MaxLab/bin/killall.sh")                         # shut down MaxOne server
            os.system("echo mxwbio | sudo -S docker stop wetai")                    # stop wetai
            mb.publish_message(topic="mcclintock/cmnd/POWER", message="OFF" )       # turn off smart plug