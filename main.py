#!/usr/bin/env python

import sys
import signal
import logging
import RPi.GPIO as GPIO
from listener import Listener
from logger_writer import LoggerWriter
from motor_controller import MotorController
from switch_controller import SwitchController

def main():
    logging.basicConfig(filename='/var/log/executioner/executioner.log', level=logging.INFO, format='%(asctime)s %(message)s')

    #not handling signals because python can't reconcile them with multithreading. supposedly Py3.3 does though.
    #signal.signal(signal.SIGINT, handle_signal)
    #signal.signal(signal.SIGTERM, handle_signal)

    sys.stdout = LoggerWriter(logging.info)
    sys.stderr = LoggerWriter(logging.error)
    MotorController.init()
    SwitchController.init()
    listener = Listener()
    listener.start()

def handle_signal(signum, stack):
    close()

def close():
    logging.info('closing gracefully')
    GPIO.cleanup()

if __name__ == "__main__":
    main()
