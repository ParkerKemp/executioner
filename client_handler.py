#!/usr/bin/env python

import time
import json
import threading
import logging
from door_controller import DoorController

class ClientHandler (threading.Thread):
  def __init__(self, sock):
    threading.Thread.__init__(self)
    self.sock = sock
  
  def run(self):
    message = self.sock.recv(1024)
    logging.info('Received message: {}.'.format(message))
    self.parse_request(message)
    self.sock.close()
   
  def parse_request(self, message):
    try:
      obj = json.loads(message)
      intent = obj['Intent']
      if intent == 'status':
        self.get_status()
      elif intent == 'set':
        newState = obj['Data']
        self.set_door(newState)
    except ValueError as err:
      logging.error('Error decoding message: {}.'.format(message))
      return None

  def get_status(self):
    status = DoorController.get_status()
    self.send_status(status, 0, True)

  def set_door(self, newState):
    if newState == 2:
      self.open_door()
    else:
      self.close_door()

  def close_door(self):
    DoorController.set_status(False)

    while DoorController.get_status() == 2:
      time.sleep(0.1)
    self.send_status(-1, 0, True)

    while DoorController.get_status() == 0:
      time.sleep(0.1)
    self.send_status(-2, 0, True)

  def open_door(self):
    DoorController.set_status(True)

    while DoorController.get_status() == -2:
      time.sleep(0.1)
    self.send_status(1, 0, True)

    while DoorController.get_status() == 0:
      time.sleep(0.1)
    self.send_status(2, 0, True)

  def send_status(self, status, lastChanged, byClient):
    obj = {}
    obj['Status'] = status
    obj['LastChanged'] = lastChanged
    obj['ChangedByClient'] = byClient
    
    s = json.dumps(obj)
    s += '\n'
    self.sock.send(s)
    logging.info('Sent message: {}'.format(s))
