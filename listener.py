#!/usr/bin/env python

import socket

listenPort = 7654

class Listener:
  def __init__(self):
    self.sock = self.__open_socket()
  
  def start(self):
    logging.info('Listening on port {}.'.format(listenPort))
    while True:
      try:
        (clientSock, (address, port)) = self.sock.accept()
        logging.info('Connecting to {}.'.format(address))
        clientHandler = ClientHandler(clientSock)
        clientHandler.start()
      except socket.error as err:
        logging.error('Encountered socket error: {}.'.format(err))

  def __open_socket(self):
    try:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      sock.bind((socket.gethostname(), listenPort))
      sock.listen(25)
      return sock
    except socket.error as err:
      return None
