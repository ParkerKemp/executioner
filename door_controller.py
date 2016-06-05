#!/usr/bin/env python

import logging
from door_simulator import DoorSimulator

class DoorController:
  #status == True when open

  def __init__(self):
    pass

  @staticmethod
  def get_status():
    top = DoorController.get_top_switch()
    bottom = DoorController.get_bottom_switch()
    if top: #Top switch is open
      return 2
    elif bottom: #Top closed, bottom open
      return 0
    else: #Both switches closed
      return -2

  @staticmethod
  def get_top_switch():
    try:
      f = open('/var/local/executioner/top_switch', 'r')
      status = f.read().strip()
      return status == "1"
    except IOError as e:
      logging.error('I/O error while reading top switch: {}.'.format(e))
      return False

  @staticmethod
  def get_bottom_switch():
    try:
      f = open('/var/local/executioner/bottom_switch', 'r')
      status = f.read().strip()
      return status == "1"
    except IOError as e:
      logging.error('I/O error while reading bottom switch: {}.'.format(e))
      return False

  
  @staticmethod
  def set_status(newStatus):
    sim = DoorSimulator(newStatus)
    sim.start()

