#!/usr/bin/env python

import json
import threading
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
        newState = obj['data']
        self.set_door(newState)
    except JsonDecodeError as err:
      logging.error('Error decoding message: {}.'.format(message))
      return None

  def get_status(self):
    status = DoorController.get_status()
    obj = {}
    obj['Open'] = status
    obj['LastChanged'] = 0
    obj['ChangedByClient'] = True

    s = json.dumps(obj)
    self.sock.send(s)

  def set_door(self, newState):
    DoorController.set_status(newState)
