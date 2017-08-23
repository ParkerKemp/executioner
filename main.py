#!/usr/bin/env python

import sys
import signal
import logging
from listener import Listener
from logger_writer import LoggerWriter
from motor_controller import MotorController
from switch_controller import SwitchController

def main():
    logging.basicConfig(filename='/var/log/executioner/executioner.log', level=logging.INFO, format='%(asctime)s %(message)s')
    signal.signal(signal.SIGINT, close)
    signal.signal(signal.SIGTERM, close)

    try:
        sys.stdout = LoggerWriter(logging.info)
        sys.stderr = LoggerWriter(logging.error)
        MotorController.init()
        SwitchController.init()
        listener = Listener()
        listener.start()
    finally:
        close()

def close():
    GPIO.cleanup()

if __name__ == "__main__":
    main()
