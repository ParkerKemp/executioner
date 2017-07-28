#!/usr/bin/env python

import sys
import logging
from listener import Listener
from logger_writer import LoggerWriter
from motor_controller import MotorController
from switch_controller import SwitchController

def main():
  logging.basicConfig(filename='/var/log/executioner/executioner.log', level=logging.INFO, format='%(asctime)s %(message)s')
  sys.stdout = LoggerWriter(logging.info)
  sys.stderr = LoggerWriter(logging.error)
  MotorController.init()
  SwitchController.init()
  listener = Listener()
  listener.start()

if __name__ == "__main__":
  main()
