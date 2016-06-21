#!/usr/bin/env python

import logging
import time
import threading
from motor_controller import MotorController

class DoorSimulator (threading.Thread):
  def __init__(self, newStatus):
    threading.Thread.__init__(self)
    self.newStatus = newStatus
    self.motor = MotorController()
    
  def run(self):
    time.sleep(0.5)
    if self.newStatus:
      self.motor.backward(50)
      self.set_bottom_switch()
      time.sleep(5)
      self.set_top_switch()
      self.motor.stop()
      self.motor.cleanup()
    else:
      self.motor.forward(50)
      self.set_top_switch()
      time.sleep(5)
      self.set_bottom_switch()
      self.motor.stop()
      self.motor.cleanup()

  def set_top_switch(self):
    f = open('/var/local/executioner/top_switch', 'w')
    if self.newStatus:
      f.write("1")
    else:
      f.write("0")
    f.close()

  def set_bottom_switch(self):
    f = open('/var/local/executioner/bottom_switch', 'w')
    if self.newStatus:
      f.write("1")
    else:
      f.write("0")
    f.close()

