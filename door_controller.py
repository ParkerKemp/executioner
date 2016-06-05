#!/usr/bin/env python

import logging

class DoorController:
  #status == True when open

  def __init__(self):
    pass

  @staticmethod
  def get_status():
    try:
      f = open('/var/local/executioner/status', 'r')
      status = f.read().strip()
      return status == "1"
    except IOError as e:
      logging.error('I/O error while reading status file: {}.'.format(e))
      DoorController.set_status(True)
      return DoorController.get_status()
    #Read input from limit switch (or stored value during testing)

  @staticmethod
  def set_status(newStatus):
    f = open('/var/local/executioner/status', 'w')
    if newStatus:
      f.write("1")
    else:
      f.write("0")
    f.close()
    #Stored value is only for testing
    #Should this block until door finishes opening/closing? With timeout and return value indicating success.
