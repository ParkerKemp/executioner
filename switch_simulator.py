#!/usr/bin/env python

import logging
import time
import threading
from configuration import DoorStatus

class SwitchSimulator (threading.Thread):
  def __init__(self, newState):
    threading.Thread.__init__(self)
    self.newState = newState
    
  def run(self):
    if self.newState == DoorStatus.Closed:
      time.sleep(2)
      self.set_switch(True)
    else:
      self.set_switch(False)

  def set_switch(self, status):
    f = open('/var/local/executioner/switch', 'w')
    if status:
      f.write("1")
    else:
      f.write("0")
    f.close()
