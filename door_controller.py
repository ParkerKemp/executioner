#!/usr/bin/env python

import logging
from motor_controller import MotorController
from switch_simulator import SwitchSimulator
from configuration import DoorStatus
from configuration import Config
from switch_controller import SwitchController

from time import sleep

class DoorController:
  #status == True when open

  def __init__(self):
    pass

  @staticmethod
  def get_status():
    return SwitchController.get_status()
    state = DoorController.get_switch_state()
    if state:
      return DoorStatus.Closed 
    else:
      return DoorStatus.Open

    return state

  @staticmethod
  def get_switch_state():
    try:
      f = open('/var/local/executioner/switch', 'r')
      status = f.read().strip()
      return status == "1"
    except IOError as e:
      logging.error('I/O error while reading switch: {}.'.format(e))
      return False

  @staticmethod
  def set_status(newStatus):
    #switch = SwitchSimulator(newStatus)
    
    #switch.start()

    if newStatus == DoorStatus.Closed:
      MotorController.energize_down()
      
      while DoorController.get_status() == DoorStatus.Open:
        sleep(0.01)
    else:
      MotorController.energize_up()
      sleep(Config.UpDuration)

    MotorController.halt()
